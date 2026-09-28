# 留样观察-qcbd_sampleobv

## 观察信息分录-子表 t_qcbd_obv_record

- **表名称：** 观察信息分录-子表
- **表名：** t_qcbd_obv_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsampleunit | 样品计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | fobvlossbaseqty | 观察损耗基本数量 | numeric | 23 | 10 | √ | 0 | 观察损耗基本数量 |
| 4 | frecorder | 记录员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fobvitem | 观察项目 | varchar | 1500 |  | √ | ' ' | 观察项目 |
| 7 | fobvrecord | 观察记录 | varchar | 150 |  | √ | ' ' | 观察记录 |
| 8 | fobvstd | 观察标准 | varchar | 1500 |  | √ | ' ' | 观察标准 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fobvitemunit | 观察项目单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fmeasureddeter | 实测值（定性） | varchar | 150 |  | √ | ' ' | 实测值（定性） |
| 12 | fitemtype | 项目类型 | varchar | 20 |  | √ | ' ' | 项目类型,枚举: A :定量 B :定性 |
| 13 | fmeasuredration | 实测值（定量） | numeric | 23 | 10 | √ | 0 | 实测值（定量） |
| 14 | fobvresult | 观察结果 | varchar | 20 |  | √ | ' ' | 观察结果,枚举: QUALITY :合格 UNQUALITY :不合格 |
| 15 | fsamplebaseunit | 样品基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fobvcontent | 观察内容 | varchar | 1500 |  | √ | ' ' | 观察内容 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fobvlossqty | 观察损耗数量 | numeric | 23 | 10 | √ | 0 | 观察损耗数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_sobvrec_fid |  | fid |
| 2 | pk_qcbd_obv_record |  | fentryid |

---

## 留样观察-主表 t_qcbd_sample_obv

- **表名称：** 留样观察-主表
- **表名：** t_qcbd_sample_obv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ftabseq | 原页签序号 | int4 | 32 |  | √ | 0 | 原页签序号 |
| 4 | fbillstatus | 记录状态 | bpchar | 1 |  | √ | 'A' | 记录状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fplanobvtime | 计划观察时间 | timestamp | 0 |  |  | null | 计划观察时间 |
| 6 | factualobvtime | 实际观察时间 | timestamp | 0 |  |  | null | 实际观察时间 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 10 | fmodifytime | 记录更新时间 | timestamp | 0 |  |  | null | 记录更新时间 |
| 11 | fledgerid | 样品台账主键 | int8 | 64 |  | √ | 0 | 样品台账主键 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_sobv_fbillno |  | fbillno |
| 2 | idx_qcbd_sobv_ftabseq |  | ftabseq |
| 3 | idx_qcbd_sobv_flb |  | fledgerid,fbillstatus |
| 4 | pk_qcbd_sample_obv |  | fid |
| 5 | idx_qcbd_sobv_fledger |  | fledgerid |
