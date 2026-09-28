# 齐套分析结果-mpdm_kitting

## 齐套分析明细-子表 t_mpdm_kittingentry

- **表名称：** 齐套分析明细-子表
- **表名：** t_mpdm_kittingentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresiduesupplyqty | 剩余供应数量_库存 | numeric | 23 | 10 | √ | 0 | 剩余供应数量_库存 |
| 3 | fexpresiduesupplybaseqty | 剩余供应基本数量_预计入 | numeric | 23 | 10 | √ | 0 | 剩余供应基本数量_预计入 |
| 4 | fentrybaseunitid | 子项基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | fclaimedqty | 可领数量 | numeric | 23 | 10 | √ | 0 | 可领数量 |
| 6 | fwaittransqty | 待调拨数量 | numeric | 23 | 10 | √ | 0 | 待调拨数量 |
| 7 | fexpectedsubtermqty | 子项预计套数 | numeric | 23 | 10 | √ | 0 | 子项预计套数 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fparentbillno | 订单编号 | varchar | 50 |  | √ | ' ' | 订单编号 |
| 10 | fparententryseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | fclaimedbaseqty | 可领基本数量 | numeric | 23 | 10 | √ | 0 | 可领基本数量 |
| 12 | fpomstockentryf7id | 生产用料清单分录F7 | int8 | 64 |  | √ | 0 | [生产用料清单分录f7 pom_mftstockentryf7](../pom_files/pom_mftstockentryf7.md) |
| 13 | fcurreceivedqty | fcurreceivedqty | numeric | 23 | 10 | √ | 0 |  |
| 14 | fdemanddate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 15 | fplanmaterialid | 物料（计划） | int8 | 64 |  | √ | 0 | [物料计划信息 mpdm_materialplan](../sbd_files/mpdm_materialplan.md) |
| 16 | fpomorderentryf7id | 生产工单分录F7 | int8 | 64 |  | √ | 0 | [生产工单分录f7 pom_mftorder_f7](../pom_files/pom_mftorder_f7.md) |
| 17 | fsubkittingsign | 子项齐套状况 | varchar | 5 |  | √ | ' ' | 子项齐套状况,枚举: A :库存齐套 B :预计齐套 C :不齐套 D :暂收齐套 E :在途齐套 F :采购申请齐套 G :计划订单齐套 |
| 18 | freplacegroup | 替代组号 | int4 | 32 |  | √ | 0 | 替代组号 |
| 19 | fresexpasstbaseqty | 剩余供应分配基本数量_预计入 | numeric | 23 | 10 | √ | 0 | 剩余供应分配基本数量_预计入 |
| 20 | fdemandbaseqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 21 | freserveexpectedbaseqty | 预留基本数量_预计入 | numeric | 23 | 10 | √ | 0 | 预留基本数量_预计入 |
| 22 | finvkittingqty | 库存齐套数量 | numeric | 23 | 10 | √ | 0 | 库存齐套数量 |
| 23 | ftaskstatus | 任务状态 | varchar | 5 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 24 | fresinvasstbaseqty | 剩余供应分配基本数量_库存 | numeric | 23 | 10 | √ | 0 | 剩余供应分配基本数量_库存 |
| 25 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 27 | fpomorderf7id | 生产工单单据头F7 | int8 | 64 |  | √ | 0 | [生产工单单据头F7 pom_mftorder_headf7](../pom_files/pom_mftorder_headf7.md) |
| 28 | fresexpasstqty | 剩余供应分配数量_预计入 | numeric | 23 | 10 | √ | 0 | 剩余供应分配数量_预计入 |
| 29 | fkittingsupplydate | 预计齐套日期 | timestamp | 0 |  |  | null | 预计齐套日期 |
| 30 | fivnassigenmenbaseqty | 齐套分配供应基本数量_库存 | numeric | 23 | 10 | √ | 0 | 齐套分配供应基本数量_库存 |
| 31 | fuseratio | 使用比例(%) | numeric | 23 | 10 | √ | 0 | 使用比例(%) |
| 32 | fpomstockf7id | 生产用料清单F7 | int8 | 64 |  | √ | 0 | [生产用料清单f7 pom_mftstockf7](../pom_files/pom_mftstockf7.md) |
| 33 | fexpassigenmenqty | 齐套分配供应数量_预计入 | numeric | 23 | 10 | √ | 0 | 齐套分配供应数量_预计入 |
| 34 | forderno | forderno | varchar | 50 |  | √ | ' ' |  |
| 35 | fkittingbaseqty | 齐套基本数量 | numeric | 23 | 10 | √ | 0 | 齐套基本数量 |
| 36 | factureceivedqty | 实领数量 | numeric | 23 | 10 | √ | 0 | 实领数量 |
| 37 | fcurtransqty | 本次调拨数量 | numeric | 23 | 10 | √ | 0 | 本次调拨数量 |
| 38 | favailablebaseqty | 可供应基本数量 | numeric | 23 | 10 | √ | 0 | 可供应基本数量 |
| 39 | fentrymasterid | 子项物料（主） | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 40 | freplacestrategy | 替代策略 | varchar | 5 |  | √ | ' ' | 替代策略,枚举: 1001 :整批替代 1002 :混用替代 1003 :整批+混用 1004 :手工替代 |
| 41 | fassignmentqty | fassignmentqty | numeric | 23 | 10 | √ | 0 |  |
| 42 | fentrylicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 43 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 44 | fexpectedsubtermbaseqty | 子项预计基本套数 | numeric | 23 | 10 | √ | 0 | 子项预计基本套数 |
| 45 | fcurclaimedqty | 本次领料数量 | numeric | 23 | 10 | √ | 0 | 本次领料数量 |
| 46 | freservebaseqty | 预留基本数量_库存 | numeric | 23 | 10 | √ | 0 | 预留基本数量_库存 |
| 47 | fmaterialid | 物料（生产） | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 48 | freplacemode | 替代方式 | varchar | 5 |  | √ | ' ' | 替代方式,枚举: A :替代 B :取代 C :按比例 |
| 49 | fpriority | 替代优先级 | int4 | 32 |  | √ | 0 | 替代优先级 |
| 50 | fexpkittingqty | 预计齐套数量 | numeric | 23 | 10 | √ | 0 | 预计齐套数量 |
| 51 | fbizstatus | 业务状态 | varchar | 5 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 D :已结算 |
| 52 | fsubunitid | 子项单位（生产） | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 53 | fexpectedsupplyqty | 预计入供应数量 | numeric | 23 | 10 | √ | 0 | 预计入供应数量 |
| 54 | fsubtermqty | 子项套数 | numeric | 23 | 10 | √ | 0 | 子项套数 |
| 55 | fresinvasstqty | 剩余供应分配数量_库存 | numeric | 23 | 10 | √ | 0 | 剩余供应分配数量_库存 |
| 56 | fexpassigenmenbaseqty | 齐套分配供应基本数量_预计入 | numeric | 23 | 10 | √ | 0 | 齐套分配供应基本数量_预计入 |
| 57 | freplaceplan | 替代方案 | int8 | 64 |  | √ | 0 | [物料替代方案 mpdm_replaceplan](../basedata_files/mpdm_replaceplan.md) |
| 58 | fcurdemandqty | 本次需求数量 | numeric | 23 | 10 | √ | 0 | 本次需求数量 |
| 59 | fsubkittingsupplydate | 供应日期 | timestamp | 0 |  |  | null | 供应日期 |
| 60 | fexpectedsupplybaseqty | 预计入供应基本数量 | numeric | 23 | 10 | √ | 0 | 预计入供应基本数量 |
| 61 | fentrymaterialid | 子项物料（生产） | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 62 | fmasterid | 物料（主） | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 63 | fprdunitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 64 | fkittingsign | 齐套状况 | varchar | 5 |  | √ | ' ' | 齐套状况,枚举: A :库存齐套 B :预计齐套 C :不齐套 D :暂收齐套 E :在途齐套 F :采购申请齐套 G :计划订单齐套 |
| 65 | finstantsupplybaseqty | 库存供应基本数量 | numeric | 23 | 10 | √ | 0 | 库存供应基本数量 |
| 66 | favailableqty | 可供应数量 | numeric | 23 | 10 | √ | 0 | 可供应数量 |
| 67 | fresiduesupplybaseqty | 剩余供应基本数量_库存 | numeric | 23 | 10 | √ | 0 | 剩余供应基本数量_库存 |
| 68 | fexpkittingbaseqty | 预计齐套基本数量 | numeric | 23 | 10 | √ | 0 | 预计齐套基本数量 |
| 69 | fentrybonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 70 | finstantsupplyqty | 库存供应数量 | numeric | 23 | 10 | √ | 0 | 库存供应数量 |
| 71 | fivnassigenmenqty | 齐套分配供应数量_库存 | numeric | 23 | 10 | √ | 0 | 齐套分配供应数量_库存 |
| 72 | forderbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :作废 |
| 73 | fexpoweqty | 预计入欠料数量 | numeric | 23 | 10 | √ | 0 | 预计入欠料数量 |
| 74 | freserveqty | 预留数量_库存 | numeric | 23 | 10 | √ | 0 | 预留数量_库存 |
| 75 | finvsubtermbaseqty | 子项库存基本套数 | numeric | 23 | 10 | √ | 0 | 子项库存基本套数 |
| 76 | fsupernovaqty | 上次齐套超发数量 | numeric | 23 | 10 | √ | 0 | 上次齐套超发数量 |
| 77 | fismainreplace | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 78 | fentryorgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 79 | fstockdemandqty | 应发数量 | numeric | 23 | 10 | √ | 0 | 应发数量 |
| 80 | fexpresiduesupplyqty | 剩余供应数量_预计入 | numeric | 23 | 10 | √ | 0 | 剩余供应数量_预计入 |
| 81 | fprdqty | 生产数量 | numeric | 23 | 10 | √ | 0 | 生产数量 |
| 82 | fdemandentryid | 需求分录ID | int8 | 64 |  | √ | 0 | 需求分录ID |
| 83 | finvsubtermqty | 子项库存齐套数 | numeric | 23 | 10 | √ | 0 | 子项库存齐套数 |
| 84 | fsubtermbaseqty | 子项基本套数 | numeric | 23 | 10 | √ | 0 | 子项基本套数 |
| 85 | fplanstatus | 计划状态 | varchar | 5 |  | √ | ' ' | 计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 86 | fkittingqty | 齐套数量 | numeric | 23 | 10 | √ | 0 | 齐套数量 |
| 87 | freserveexpectedqty | 预留数量_预计入 | numeric | 23 | 10 | √ | 0 | 预留数量_预计入 |
| 88 | finvkittingbaseqty | 库存齐套基本数量 | numeric | 23 | 10 | √ | 0 | 库存齐套基本数量 |
| 89 | ftaskentryid | 任务分录ID | int8 | 64 |  | √ | 0 | 任务分录ID |
| 90 | fdemandqty | 剩余需求数量 | numeric | 23 | 10 | √ | 0 | 剩余需求数量 |
| 91 | fwaitclaimedqty | 待领数量 | numeric | 23 | 10 | √ | 0 | 待领数量 |
| 92 | fbaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 93 | finvoweqty | 库存欠料数量 | numeric | 23 | 10 | √ | 0 | 库存欠料数量 |

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
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
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
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织（废弃） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmaterialreplace | 物料替代 | varchar | 30 |  | √ | ' ' | 物料替代,枚举: A :考虑替代 B :忽略替代 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fkittinganalysisid | 齐套分析方案 | int8 | 64 |  | √ | 0 | [齐套分析方案 mpdm_kitting_analysis](../mpdm_files/mpdm_kitting_analysis.md) |
| 10 | fanalysistype | 分析方式 | varchar | 30 |  | √ | ' ' | 分析方式,枚举: A :齐套分析 B :齐套分析+创建强预留 C :齐套分析+创建弱预留 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmaterialrange | 物料范围 | varchar | 30 |  | √ | ' ' | 物料范围,枚举: A :全部物料 B :非倒冲物料 C :关键物料 |
| 13 | fpreferred | 优选顺序 | varchar | 30 |  | √ | ' ' | 优选顺序,枚举: A :计划开工时间 B :计划完工时间 C :需求优先级 |
| 14 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_kitting |  | fid |
