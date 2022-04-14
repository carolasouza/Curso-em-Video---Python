# Cores no TERMINAL
# Código padrão ANSI que é compatível com o Python
# SINTAXE:
# \033[ ; ; m -> sintaxe padrão para colorir o terminal
# há 3 parâmetros que precisam ser preenchidos dentro dos espaços

# primeiro: style -> estilo do texto
    # 0 = None (sem estilo nenhum); 1 = bold; 4 = underline; 7 = negative (inverte as cores de texto e fundo)

    # ESC Code Sequence	    Reset Sequence	Description
    # ESC[1;34;{...}m		                Set graphics modes for cell, separated by semicolon (;).
    # ESC[0m		                        reset all modes (styles and colors)
    # ESC[1m	            ESC[22m	        set bold mode.
    # ESC[2m	            ESC[22m	        set dim/faint mode.
    # ESC[3m	            ESC[23m	        set italic mode.
    # ESC[4m	            ESC[24m	        set underline mode.
    # ESC[5m	            ESC[25m	        set blinking mode
    # ESC[7m	            ESC[27m	        set inverse/reverse mode
    # ESC[8m	            ESC[28m	        set hidden/invisible mode
    # ESC[9m	            ESC[29m	        set strikethrough mode.

# segundo: text -> cor da letra
# terceiro: back -> cor de fundo do texto (mesma ordem de cores do text, começando com 4)

    # Color Name	Foreground Color Code	Background Color Code
    # Black	        30	                    40
    # Red	        31	                    41
    # Green	        32	                    42
    # Yellow	    33	                    43
    # Blue	        34	                    44
    # Magenta	    35	                    45
    # Cyan	        36	                    46
    # Gray	        37  	                47
    # White         97                      107
    # Default	    39	                    49
    # Reset	        0	                    0

print('\033[0;97;41mTeste')
print('\033[4;33;44mTeste')
print('\033[1;35;43mTeste')
print('\033[97;42mTeste')
print('\033[0mTeste')
print('\033[7;97;40mTeste')
