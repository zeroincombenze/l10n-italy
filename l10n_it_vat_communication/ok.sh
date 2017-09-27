ver='7.0'
echo "cd ~/$ver/l10n-italy/l10n_it_vat_communication"
cd ~/$ver/l10n-italy/l10n_it_vat_communication
echo "find . -type f \( -name \"*.py\" -o -name \"*.xml\" \) -exec sed -e \"s/vat_period_end_statement/vat_communication/g\" -i '{}' \;"
find . -type f \( -name "*.py" -o -name "*.xml" \) -exec sed -e "s/vat_period_end_statement/vat_communication/g" -i '{}' \;
echo "find . -type f \( -name \"*.py\" -o -name \"*.xml\" \) -exec sed -e \"s/vat\.period\.end\.statement/vat.communication/g\" -i '{}' \;"
find . -type f \( -name "*.py" -o -name "*.xml" \) -exec sed -e "s/vat\.period\.end\.statement/vat.communication/g" -i '{}' \;
