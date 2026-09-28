# 齐套分析结果-mpdm_kitting

## 单据体-子表 t_mpdm_kittingentry

- **表名称：** 单据体-子表
- **表名：** t_mpdm_kittingentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresiduesupplyqty | 剩余供应数量 | numeric | 23 | 10 | √ | 0 | 剩余供应数量 |
| 3 | fentrybaseunitid | 子项基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 4 | fclaimedqty | 可领数量 | numeric | 23 | 10 | √ | 0 | 可领数量 |
| 5 | fcurclaimedqty | 本次领料数量 | numeric | 23 | 10 | √ | 0 | 本次领料数量 |
| 6 | fwaittransqty | 待调拨数量 | numeric | 23 | 10 | √ | 0 | 待调拨数量 |
| 7 | freservebaseqty | 预留基本数量 | numeric | 23 | 10 | √ | 0 | 预留基本数量 |
| 8 | fmaterialid | 物料（生产） | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fparentbillno | 订单编号 | varchar | 50 |  | √ | ' ' | 订单编号 |
| 11 | fsubunitid | 子项单位（生产） | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fparententryseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 13 | fsubtermqty | 子项套数 | numeric | 23 | 10 | √ | 0 | 子项套数 |
| 14 | fclaimedbaseqty | 可领基本数量 | numeric | 23 | 10 | √ | 0 | 可领基本数量 |
| 15 | fcurreceivedqty | fcurreceivedqty | numeric | 23 | 10 | √ | 0 |  |
| 16 | fdemanddate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 17 | fplanmaterialid | 物料（计划） | int8 | 64 |  | √ | 0 | 物料计划信息 mpdm_materialplan |
| 18 | fentrymaterialid | 子项物料（生产） | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 19 | fmasterid | 物料（主） | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 20 | fprdunitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fdemandbaseqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 22 | finstantsupplybaseqty | 即时供应基本数量 | numeric | 23 | 10 | √ | 0 | 即时供应基本数量 |
| 23 | favailableqty | 可供应数量 | numeric | 23 | 10 | √ | 0 | 可供应数量 |
| 24 | fresiduesupplybaseqty | 剩余供应基本数量 | numeric | 23 | 10 | √ | 0 | 剩余供应基本数量 |
| 25 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 26 | finstantsupplyqty | 即时供应数量 | numeric | 23 | 10 | √ | 0 | 即时供应数量 |
| 27 | freserveqty | 预留数量 | numeric | 23 | 10 | √ | 0 | 预留数量 |
| 28 | fsupernovaqty | 超发数量 | numeric | 23 | 10 | √ | 0 | 超发数量 |
| 29 | fentryorgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fprdqty | 生产数量 | numeric | 23 | 10 | √ | 0 | 生产数量 |
| 31 | forderno | forderno | varchar | 50 |  | √ | ' ' |  |
| 32 | fsubtermbaseqty | 子项基本套数 | numeric | 23 | 10 | √ | 0 | 子项基本套数 |
| 33 | fkittingbaseqty | 齐套基本数量 | numeric | 23 | 10 | √ | 0 | 齐套基本数量 |
| 34 | factureceivedqty | 已领数量 | numeric | 23 | 10 | √ | 0 | 已领数量 |
| 35 | fkittingqty | 齐套数量 | numeric | 23 | 10 | √ | 0 | 齐套数量 |
| 36 | fcurtransqty | 本次调拨数量 | numeric | 23 | 10 | √ | 0 | 本次调拨数量 |
| 37 | favailablebaseqty | 可供应基本数量 | numeric | 23 | 10 | √ | 0 | 可供应基本数量 |
| 38 | fentrymasterid | 子项物料（主） | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 39 | fassignmentqty | fassignmentqty | numeric | 23 | 10 | √ | 0 |  |
| 40 | fdemandqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 41 | fwaitclaimedqty | 待领数量 | numeric | 23 | 10 | √ | 0 | 待领数量 |
| 42 | fbaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 43 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kittingentry_fid |  | fid |
| 2 | pk_kittingentry |  | fentryid |

---

## 组织-多选基础资料表 t_mpdm_kittingorgs

- **表名称：** 组织-多选基础资料表
- **表名：** t_mpdm_kittingorgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_kittingorgs |  | fpkid |
| 2 | idx_mpdm_kittingorgs_id |  | fid |

---

## 齐套分析结果-主表 t_mpdm_kitting

- **表名称：** 齐套分析结果-主表
- **表名：** t_mpdm_kitting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织（废弃） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmaterialreplace | 物料替代 | varchar | 30 |  | √ | ' ' | 物料替代,枚举: A :考虑替代 B :忽略替代 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fanalysistype | 分析方式 | varchar | 30 |  | √ | ' ' | 分析方式,枚举: A :库存齐套分析 B :库存齐套分析+预留 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmaterialrange | 物料范围 | varchar | 30 |  | √ | ' ' | 物料范围,枚举: A :全部物料 B :非倒冲物料 C :关键物料 |
| 12 | fpreferred | 优选顺序 | varchar | 30 |  | √ | ' ' | 优选顺序,枚举: A :计划开工时间 B :计划完工时间 C :需求优先级 |
| 13 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_kitting |  | fid |
