#!/usr/bin/env python3
# -*- coding: utf-8 -*-

category = 'Test'

class Driver_parser():
    def __init__(self, Instance, name, **kwargs):
        self.name     = name
        self.Instance = Instance


    def add_parser_usage(self,message):
        """Usage to be used by the parser"""
        usage = f"""
{message}

----------------  Examples:  ----------------

usage:    autolab driver [options] args

    autolab driver -D {self.name} -A 192.168.0.8 -C CONN -m some_methods
    Execute some_methods of the driver. A list of available methods is present at the top of this help.

    autolab driver -D nickname -m some_methods
    Same as before using the nickname defined in devices_index.ini
            """
        return usage

    def add_parser_arguments(self,parser):
        """Add arguments to the parser passed as input"""
        # BUG: Only use type=str not bool or other because OS Shell is always str so will do bool('0') or bool('1') which is always True
        parser.add_argument("-verb", "--verbose", type=str, dest="verbose", default=None, help="Set verbose")
        parser.add_argument("-a", "--amplitude", type=str, dest="amplitude", default=None, help="Set the amplitude" )
        #parser.add_argument("-c", "--channels", type=str, dest="channels", default=None, help="Set the traces to act on/acquire from." )
        #parser.add_argument("-o", "--filename", type=str, dest="filename", default=None, help="Set the name of the output file" )
        #parser.add_argument("-F", "--force",action="store_true", dest="force", default=None, help="Allows overwriting file" )
        #parser.add_argument("-t", "--trigger", dest="trigger",action="store_true", help="Trigger the scope once" )

        return parser

    def do_something(self,args):
        # OPTIMIZE: If sequential order of args is important, could do a for loop in args to get the proper order. But if function order is more important, define the condition bellow to match your desired order.
        if args.verbose:
            getattr(self.Instance,'set_verbose')(args.verbose)
        if args.amplitude:
            getattr(self.Instance,'set_amplitude')(args.amplitude)
        #if args.filename:
            ##getattr(self.Instance,'get_data_traces')(traces=args.channels,single=args.trigger)
            #getattr(self.Instance,'get_data_traces')(traces=args.channels)
            #getattr(self.Instance,'save_data_traces')(filename=args.filename,traces=args.channels,FORCE=args.force)
        pass

    def exit(self):
        self.Instance.close()
        pass
