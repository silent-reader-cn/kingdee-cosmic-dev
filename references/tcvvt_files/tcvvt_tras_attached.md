# 重点税源报表附表-tcvvt_tras_attached

## 重点税源报表附表-主表 t_tcvvt_tras_attached

- **表名称：** 重点税源报表附表-主表
- **表名：** t_tcvvt_tras_attached

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 3 | fzjgorg | 总机构名称 | int8 | 64 |  | √ | 0 | 税务组织信息 bastax_taxorg |
| 4 | ftbsnysjwcmc | 填报上年下月实际完成名称 | varchar | 30 |  | √ | ' ' | 填报上年下月实际完成名称 |
| 5 | fbnmc | 本年名称 | varchar | 50 |  | √ | ' ' | 本年名称 |
| 6 | fsnmc | 上年名称 | varchar | 50 |  | √ | ' ' | 上年名称 |
| 7 | fhhsyqqqssjjlx | 混合所有制企业所属经济类型 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_zdsy_bizdefen_tree |
| 8 | fjtgsqk | 集团公司情况 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_zdsy_bizdefen_tree |
| 9 | fxfsjnfs | 消费税缴纳方式 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_zdsy_bizdefen_tree |
| 10 | fzzsyhzcxs | 增值税优惠政策形式 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_zdsy_bizdefen_tree |
| 11 | fqycwhsfsjbbq | 企业财务核算方式及报表期 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_zdsy_bizdefen_tree |
| 12 | fcjjc | 采集级次 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_zdsy_bizdefen_tree |
| 13 | fzrrtzbl | 自然人投资比例（%） | numeric | 23 | 10 | √ | 0 | 自然人投资比例（%） |
| 14 | fssgfdm | 上市股票代码 | varchar | 50 |  | √ | ' ' | 上市股票代码 |
| 15 | fqysdsdeadline | 企业所得税申报周期(企业所得税卡片缴纳期限) | varchar | 50 |  | √ | ' ' | 企业所得税申报周期(企业所得税卡片缴纳期限),枚举: 0 :不申报 1 :按月申报 2 :按季申报 |
| 16 | ftbnqnycmc | 填报年全年预测名称 | varchar | 30 |  | √ | ' ' | 填报年全年预测名称 |
| 17 | fsnyljmc | 上年月累计名称 | varchar | 50 |  | √ | ' ' | 上年月累计名称 |
| 18 | fqysdsyhzcxs | 企业所得税优惠政策形式 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_zdsy_bizdefen_tree |
| 19 | fzjgnsrmc | 总机构统一社会信用代码（纳税人识别号） | varchar | 50 |  | √ | ' ' | 总机构统一社会信用代码（纳税人识别号） |
| 20 | fzzsdeadline | 增值税申报周期 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_zdsy_bizdefen_tree |
| 21 | fwztzbl | 外资投资比例（%） | numeric | 23 | 10 | √ | 0 | 外资投资比例（%） |
| 22 | fxfszypm | 消费税主要品目 | int8 | 64 |  | √ | 0 | 征收品目 tpo_zspm |
| 23 | fqygm | 企业规模（工业和信息化部标准） | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_zdsy_bizdefen_tree |
| 24 | fzzscktsfs | 增值税出口退税方式 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_zdsy_bizdefen_tree |
| 25 | fyqmmc | 月期末名称 | varchar | 50 |  | √ | ' ' | 月期末名称 |
| 26 | fcreatename | 填报人姓名 | varchar | 50 |  | √ | ' ' | 填报人姓名 |
| 27 | fewblname | 二维表行名称 | varchar | 50 |  | √ | ' ' | 二维表行名称 |
| 28 | fregistertime | 企业营业执照的登记时间 | timestamp | 0 |  |  | null | 企业营业执照的登记时间 |
| 29 | fbnyljmc | 本年月累计名称 | varchar | 50 |  | √ | ' ' | 本年月累计名称 |
| 30 | fsfzmqqy | 是否自贸区企业 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_zdsy_bizdefen_tree |
| 31 | fzytzfcountry | 主要投资方所属国家或地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 32 | fzyckgj | 主要出口国家（地区） | varchar | 200 |  | √ | ' ' | 主要出口国家（地区） |
| 33 | fzxqyhjzzhzz | 执行企业会计制度或准则 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_zdsy_bizdefen_tree |
| 34 | fgytzbl | 国有投资比例（%） | numeric | 23 | 10 | √ | 0 | 国有投资比例（%） |
| 35 | fdeadline | (废弃)增值税申报周期(增值税卡片缴纳期限) | varchar | 50 |  | √ | ' ' | (废弃)增值税申报周期(增值税卡片缴纳期限),枚举: acsb :按次申报 aysb :按月申报 ajsb :按季申报 |
| 36 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 37 | fqysdsjnfs | 企业所得税缴纳方式 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_zdsy_bizdefen_tree |
| 38 | fssqyjt | 所属企业集团 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_zdsy_bizdefen_tree |
| 39 | fssgsssdq | 上市公司上市地区 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_zdsy_bizdefen_tree |
| 40 | ftbnyycmc | 填报年下月预测名称 | varchar | 30 |  | √ | ' ' | 填报年下月预测名称 |
| 41 | fzzsjnfs | 增值税缴纳方式 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_zdsy_bizdefen_tree |
| 42 | ftbsnqnsjmc | 填报上年全年实际名称 | varchar | 30 |  | √ | ' ' | 填报上年全年实际名称 |
| 43 | fqyjyzt | 企业经营状态 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_zdsy_bizdefen_tree |
| 44 | fcwfzr | 财务负责人 | varchar | 50 |  | √ | ' ' | 财务负责人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_tras_ewb |  | fewblxh,fewblname |
| 2 | idx_tcvvt_tras_sbbid |  | fsbbid |
| 3 | pk_tcvvt_tras_attached |  | fid |
