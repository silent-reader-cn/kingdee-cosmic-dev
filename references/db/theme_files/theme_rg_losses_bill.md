# 非经常性损益分析表-theme_rg_losses_bill

## 非经常性损益分析表-主表 t_theme_losses_bill

- **表名称：** 非经常性损益分析表-主表
- **表名：** t_theme_losses_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffundoccupancy | 资金占用费 | numeric | 23 | 10 |  | null | 资金占用费 |
| 3 | foperatingamount | 其他营业外收支净额 | numeric | 23 | 10 |  | null | 其他营业外收支净额 |
| 4 | fprlossinvestment | 委托投资损益占比 | numeric | 23 | 10 |  | null | 委托投资损益占比 |
| 5 | fprlossmonetary | 非货币性资产交换损益占比 | numeric | 23 | 10 |  | null | 非货币性资产交换损益占比 |
| 6 | fprlossesgains | 交易产生的损益占比 | numeric | 23 | 10 |  | null | 交易产生的损益占比 |
| 7 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 8 | fproperatingamount | 其他营业外收支净额占比 | numeric | 23 | 10 |  | null | 其他营业外收支净额占比 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |
| 11 | fprrefundreduction | 税收返还、减免占比 | numeric | 23 | 10 |  | null | 税收返还、减免占比 |
| 12 | fprlfinancialliabilities | 持有(或处置)交易性金融资产和负债产生的变动损益或投资收益占比 | numeric | 23 | 10 |  | null | 持有(或处置)交易性金融资产和负债产生的变动损益或投资收益占比 |
| 13 | fprlossrealestate | 公允价值计量的投资性房地产价值变动损占比 | numeric | 23 | 10 |  | null | 公允价值计量的投资性房地产价值变动损占比 |
| 14 | fprcorporatecost | 企业重组费用占比 | numeric | 23 | 10 |  | null | 企业重组费用占比 |
| 15 | flossloan | 对外委托贷款取得的损益 | numeric | 23 | 10 |  | null | 对外委托贷款取得的损益 |
| 16 | fprlossloan | 对外委托贷款取得的损益占比 | numeric | 23 | 10 |  | null | 对外委托贷款取得的损益占比 |
| 17 | ftotalprofit | 总利润 | numeric | 23 | 10 |  | null | 总利润 |
| 18 | fgovernmentgrants | 政府补助 | numeric | 23 | 10 |  | null | 政府补助 |
| 19 | fprcustodyfee | 受托经营取得的托管费收入占比 | numeric | 23 | 10 |  | null | 受托经营取得的托管费收入占比 |
| 20 | flossliabilities | 同一控制下企业合并产生的子公司当期净损益 | numeric | 23 | 10 |  | null | 同一控制下企业合并产生的子公司当期净损益 |
| 21 | fprcurrentassets | 非流动资产处置损益占比 | numeric | 23 | 10 |  | null | 非流动资产处置损益占比 |
| 22 | flossesdebt | 债务重组损益 | numeric | 23 | 10 |  | null | 债务重组损益 |
| 23 | fprlossliabilities | 同一控制下企业合并产生的子公司当期净损益占比 | numeric | 23 | 10 |  | null | 同一控制下企业合并产生的子公司当期净损益占比 |
| 24 | fprlosscurrent | 法律要求的对当期损益进行一次性调整的影响占比 | numeric | 23 | 10 |  | null | 法律要求的对当期损益进行一次性调整的影响占比 |
| 25 | fprfundoccupancy | 资金占用费占比 | numeric | 23 | 10 |  | null | 资金占用费占比 |
| 26 | fprestimatedliabilities | 预计负债产生的损益占比 | numeric | 23 | 10 |  | null | 预计负债产生的损益占比 |
| 27 | fprojectscsrc | 中国证监会认定的其他项目 | numeric | 23 | 10 |  | null | 中国证监会认定的其他项目 |
| 28 | fprlossmeans | 资产减值损益占比 | numeric | 23 | 10 |  | null | 资产减值损益占比 |
| 29 | fprsinglereceivables | 单独进行减值测试的应收款项减值准备转回占比 | numeric | 23 | 10 |  | null | 单独进行减值测试的应收款项减值准备转回占比 |
| 30 | flfinancialliabilities | 持有(或处置)交易性金融资产和负债产生的变动损益或投资收益 | numeric | 23 | 10 |  | null | 持有(或处置)交易性金融资产和负债产生的变动损益或投资收益 |
| 31 | flossinvestment | 委托投资损益 | numeric | 23 | 10 |  | null | 委托投资损益 |
| 32 | flossesgains | 交易产生的损益 | numeric | 23 | 10 |  | null | 交易产生的损益 |
| 33 | flossrealestate | 公允价值计量的投资性房地产价值变动损 | numeric | 23 | 10 |  | null | 公允价值计量的投资性房地产价值变动损 |
| 34 | fcustodyfee | 受托经营取得的托管费收入 | numeric | 23 | 10 |  | null | 受托经营取得的托管费收入 |
| 35 | fprlossesdebt | 债务重组损益占比 | numeric | 23 | 10 |  | null | 债务重组损益占比 |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fprprojectscsrc | 中国证监会认定的其他项目占比 | numeric | 23 | 10 |  | null | 中国证监会认定的其他项目占比 |
| 39 | fcorporatecost | 企业重组费用 | numeric | 23 | 10 |  | null | 企业重组费用 |
| 40 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 41 | fprojecttotal | 非经常性损益项目合计 | numeric | 23 | 10 |  | null | 非经常性损益项目合计 |
| 42 | frefundreduction | 税收返还、减免 | numeric | 23 | 10 |  | null | 税收返还、减免 |
| 43 | flossmonetary | 非货币性资产交换损益 | numeric | 23 | 10 |  | null | 非货币性资产交换损益 |
| 44 | flosscombination | 企业合并产生的损益 | numeric | 23 | 10 |  | null | 企业合并产生的损益 |
| 45 | festimatedliabilities | 预计负债产生的损益 | numeric | 23 | 10 |  | null | 预计负债产生的损益 |
| 46 | fprojectprofitrate | 非经常性损益占利润总额比例（%） | numeric | 23 | 10 |  | null | 非经常性损益占利润总额比例（%） |
| 47 | flossmeans | 资产减值损益 | numeric | 23 | 10 |  | null | 资产减值损益 |
| 48 | fsinglereceivables | 单独进行减值测试的应收款项减值准备转回 | numeric | 23 | 10 |  | null | 单独进行减值测试的应收款项减值准备转回 |
| 49 | fprgovernmentgrants | 政府补助占比 | numeric | 23 | 10 |  | null | 政府补助占比 |
| 50 | fcurrentassets | 非流动资产处置损益 | numeric | 23 | 10 |  | null | 非流动资产处置损益 |
| 51 | flosscurrent | 法律要求的对当期损益进行一次性调整的影响 | numeric | 23 | 10 |  | null | 法律要求的对当期损益进行一次性调整的影响 |
| 52 | fprlosscombination | 企业合并产生的损益占比 | numeric | 23 | 10 |  | null | 企业合并产生的损益占比 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_losses_bill_report |  | freportdate,fipoorgld |
| 2 | pk_theme_losses_bill |  | fid |
