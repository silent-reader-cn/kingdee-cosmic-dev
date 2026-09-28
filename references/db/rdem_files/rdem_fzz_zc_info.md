# 辅助账支出信息表(废弃)-rdem_fzz_zc_info

## 辅助账支出信息表(废弃)-主表 t_rdem_fzz_zc_info

- **表名称：** 辅助账支出信息表(废弃)-主表
- **表名：** t_rdem_fzz_zc_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjehjqtxj | 金额合计其他相关费用合计 | numeric | 23 | 2 | √ | 0 | 金额合计其他相关费用合计 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 |
| 4 | fxmmc | 项目名称 | varchar | 200 |  | √ | ' ' | 项目名称 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fjehjsfgd | 金额合计税法规定的归集金额 | numeric | 23 | 2 | √ | 0 | 金额合计税法规定的归集金额 |
| 7 | fpaytype | 支出类型（枚举） | varchar | 50 |  | √ | ' ' | 支出类型（枚举）,枚举: capital :资本化 cost :费用化 |
| 8 | fjehjkjpzjz | 金额合计会计凭证记载金额 | numeric | 23 | 2 | √ | 0 | 金额合计会计凭证记载金额 |
| 9 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 10 | fjehjryrgxj | 金额合计人员人工费用 | numeric | 23 | 2 | √ | 0 | 金额合计人员人工费用 |
| 11 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 12 | fzclx | 支出类型 | varchar | 50 |  | √ | ' ' | 支出类型 |
| 13 | feprojectstatus | 完成情况（枚举） | varchar | 50 |  | √ | ' ' | 完成情况（枚举）,枚举: 0 :未完成 1 :已完成 |
| 14 | fjehjjnjgxj | 金额合计委托境内机构或个人进行研发活动所发生的费用 | numeric | 23 | 2 | √ | 0 | 金额合计委托境内机构或个人进行研发活动所发生的费用 |
| 15 | fjehjzjfyxj | 金额合计折旧费用 | numeric | 23 | 2 | √ | 0 | 金额合计折旧费用 |
| 16 | fxmbh | 项目编号 | varchar | 200 |  | √ | ' ' | 项目编号 |
| 17 | fjehjwtjwjgxj | 金额合计委托境外机构进行研发活动所发生的费用 | numeric | 23 | 2 | √ | 0 | 金额合计委托境外机构进行研发活动所发生的费用 |
| 18 | fjehjzhtrxj | 金额合计直接投入费用 | numeric | 23 | 2 | √ | 0 | 金额合计直接投入费用 |
| 19 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 20 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 21 | fwcqk | 完成情况 | varchar | 50 |  | √ | ' ' | 完成情况 |
| 22 | fsbxm | 申报项目基础资料 | int8 | 64 |  | √ | 0 | [申报项目信息 rdem_sbxmxx](../rdem_files/rdem_sbxmxx.md) |
| 23 | fjehjwxzctxxj | 金额合计无形资产摊销 | numeric | 23 | 2 | √ | 0 | 金额合计无形资产摊销 |
| 24 | fjehjxcpsjfxj | 金额合计新产品设计费等 | numeric | 23 | 2 | √ | 0 | 金额合计新产品设计费等 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_fzz_zc_info_m0 |  | fsbxm |
| 2 | pk_rdem_fzz_zc_info |  | fid |
