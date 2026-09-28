# 配送计划处理-pom_distribplan

## 配送计划处理-主表 t_pom_distribplanx

- **表名称：** 配送计划处理-主表
- **表名：** t_pom_distribplanx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funsendqty | 未配送数量 | numeric | 23 | 10 | √ | 0 | 未配送数量 |
| 3 | fsupplyorg | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | freqtime | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 5 | fclosetype | 状态 | varchar | 5 |  | √ | ' ' | 状态,枚举: A :正常 B :手工关闭 C :运算关闭 |
| 6 | fstocklocat | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fprodmaterial | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 10 | fclosetime | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fsendedqty | 已配送数量 | numeric | 23 | 10 | √ | 0 | 已配送数量 |
| 16 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | freqorg | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fmftno | 生产工单号 | varchar | 80 |  | √ | ' ' | 生产工单号 |
| 20 | fworkproc | 工序名称 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fworkcenter | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 23 | fworkstation | 工位 | int8 | 64 |  | √ | 0 | [工位 mpdm_workstation](../mpdm_files/mpdm_workstation.md) |
| 24 | fwarehouse | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 25 | fprodunit | 产品单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | freqqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 27 | fproject | 项目号 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 28 | fcansendqty | 可配送数量 | numeric | 23 | 10 | √ | 0 | 可配送数量 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_distribplanx |  | fid |
| 2 | idx_pom_distribplanx_id |  | fbillstatus |

---

## 单据体-子表 t_pom_distribplanxent

- **表名称：** 单据体-子表
- **表名：** t_pom_distribplanxent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrymodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fprodorg | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fmtunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | funsqty | 未配送数量 | numeric | 23 | 10 | √ | 0 | 未配送数量 |
| 7 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | fcansqty | 可配送数量 | numeric | 23 | 10 | √ | 0 | 可配送数量 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fprodmtno | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 11 | fwrhouse | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 12 | fsourcebillenrtyid | 来源单据分录ID | varchar | 80 |  | √ | ' ' | 来源单据分录ID |
| 13 | fsourcebillname | 来源单据标识 | varchar | 100 |  | √ | ' ' | 来源单据标识 |
| 14 | fwkcenter | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 15 | fsourcebillentryname | 来源单据分录标识 | varchar | 100 |  | √ | ' ' | 来源单据分录标识 |
| 16 | fispushed | 是否下推 | bpchar | 1 |  | √ | '0' | 是否下推 |
| 17 | fsourcebillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 18 | fstockloc | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 19 | fsuporg | 供货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fownorg | 货主 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fwkstation | 工位 | int8 | 64 |  | √ | 0 | [工位 mpdm_workstation](../mpdm_files/mpdm_workstation.md) |
| 22 | fentrycreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fwkproc | 工序名称 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 25 | feclosetype | 状态 | varchar | 80 |  | √ | ' ' | 状态,枚举: A :正常 B :手工关闭 C :运算关闭 |
| 26 | fsourcebillid | 来源单据ID | varchar | 80 |  | √ | ' ' | 来源单据ID |
| 27 | fentpropject | 项目号 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 28 | frqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fsedqty | 已配送数量 | numeric | 23 | 10 | √ | 0 | 已配送数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_distribplanxent |  | fentryid |
| 2 | idx_pom_distribplanxent_id |  | fid |
