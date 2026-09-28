# 资源税税源采集信息-tcret_zys_collect

## 单据体-子表 t_tcret_zys_collect_en

- **表名称：** 单据体-子表
- **表名：** t_tcret_zys_collect_en

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 3 | ftaxitem | 税目 | int8 | 64 |  | √ | 0 | 资源税税率表分录 tpo_zys_taxitem_entry |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fgjje | 准予扣减的外购应税产品的购进金额 | numeric | 23 | 10 | √ | 0 | 准予扣减的外购应税产品的购进金额 |
| 6 | fbizname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 7 | fyzf | 准予扣除的运杂费 | numeric | 23 | 10 | √ | 0 | 准予扣除的运杂费 |
| 8 | fybtse | 应补（退）税额 | numeric | 23 | 10 | √ | 0 | 应补（退）税额 |
| 9 | fxse | 销售额 | numeric | 23 | 10 | √ | 0 | 销售额 |
| 10 | ftaxdeduction | 减免政策代码及名称 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 11 | fruleid | 规则id | varchar | 50 |  | √ | ' ' | 规则id |
| 12 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0 | 应纳税额 |
| 13 | fyjse | 已缴税额 | numeric | 23 | 10 | √ | 0 | 已缴税额 |
| 14 | fjsxse | 计税销售额 | numeric | 23 | 10 | √ | 0 | 计税销售额 |
| 15 | ftaxsubitem | 子目 | varchar | 50 |  | √ | ' ' | 子目,枚举: yk :原矿 xk :选矿 |
| 16 | fjmsxssl | 减免税销售数量 | numeric | 23 | 10 | √ | 0 | 减免税销售数量 |
| 17 | fjsxssl | 计税销售数量 | numeric | 23 | 10 | √ | 0 | 计税销售数量 |
| 18 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | flevy | 计征方式 | varchar | 50 |  | √ | ' ' | 计征方式,枚举: cljz :从量计征 cjjz :从价计征 |
| 20 | fxssl | 销售数量 | numeric | 23 | 10 | √ | 0 | 销售数量 |
| 21 | fgjsl | 准予扣减的外购应税产品购进数量 | numeric | 23 | 10 | √ | 0 | 准予扣减的外购应税产品购进数量 |
| 22 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 23 | fjmsxse | 减免税销售额 | numeric | 23 | 10 | √ | 0 | 减免税销售额 |
| 24 | fjmse | 减免税额 | numeric | 23 | 10 | √ | 0 | 减免税额 |
| 25 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: auto :自动取数 useradd :手工录入 import :模板引入 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | funit | 计量单位 | varchar | 200 |  | √ | ' ' | 计量单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_zys_collect_en_fk |  | fid |
| 2 | pk_tcret_zys_collect_en |  | fentryid |

---

## 资源税税源采集信息-主表 t_tcret_zys_collect

- **表名称：** 资源税税源采集信息-主表
- **表名：** t_tcret_zys_collect

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fisxgm | 是否小规模 | bpchar | 1 |  | √ | '0' | 是否小规模 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | ftaxsource | 税源编号 | int8 | 64 |  | √ | 0 | [资源税税源登记信息 tcret_zys_register](../tcret_files/tcret_zys_register.md) |
| 12 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 13 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | [纳税申报表基础资料 bdtaxr_nsrxx](../bdtaxr_files/bdtaxr_nsrxx.md) |
| 14 | ftaxoffice | 税源所属税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_zys_collect_forgid |  | forgid,ftaxoffice,fskssqz,fskssqq,ftaxsource |
| 2 | pk_tcret_zys_collect |  | fid |
