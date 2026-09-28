# 销售毛利分析中间结果-sm_salprofitmidresult

## 销售毛利分析中间结果-主表 t_sm_salprofitmidresult

- **表名称：** 销售毛利分析中间结果-主表
- **表名：** t_sm_salprofitmidresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcustomer | 订货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 3 | ftaxsalamount | 销售收入 | numeric | 23 | 10 | √ | 0 | 销售收入 |
| 4 | flocalverifyamt | 勾稽金额 | numeric | 23 | 10 | √ | 0 | 勾稽金额 |
| 5 | fsalgrossprofit | 销售毛利 | numeric | 23 | 10 | √ | 0 | 销售毛利 |
| 6 | fcurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 8 | fbizoperator | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 9 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 10 | fbaseunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 12 | forg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fsalorg | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | funitcost | 单位成本 | numeric | 23 | 10 | √ | 0 | 单位成本 |
| 15 | freporttask | 报表任务 | int8 | 64 |  | √ | 0 | 报表任务 |
| 16 | factualcost | 销售成本 | numeric | 23 | 10 | √ | 0 | 销售成本 |
| 17 | fbusamount | 暂估金额 | numeric | 23 | 10 | √ | 0 | 暂估金额 |
| 18 | fgroup | 物料分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 19 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 20 | fbaseqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 21 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 22 | fsalamount | 销售收入(不含税) | numeric | 23 | 10 | √ | 0 | 销售收入(不含税) |
| 23 | funitgrossprofit | 单位毛利 | numeric | 23 | 10 | √ | 0 | 单位毛利 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_salpr_freptask |  | freporttask |
| 2 | pk_t_sm_salprofitmidresult |  | fid |
