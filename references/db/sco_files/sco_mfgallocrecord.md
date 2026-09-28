# 制造费用分配中间计算结果表-sco_mfgallocrecord

## 制造费用分配中间计算结果表-主表 t_sco_mfgallocrecord

- **表名称：** 制造费用分配中间计算结果表-主表
- **表名：** t_sco_mfgallocrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftotalamount | 总费用金额 | numeric | 23 | 10 | √ | 0 | 总费用金额 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | ftotalstdvalue | 总分配标准值 | numeric | 23 | 10 | √ | 0 | 总分配标准值 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmfgallocbillno | 分配单单据编号 | varchar | 80 |  | √ | ' ' | 分配单单据编号 |
| 12 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_mfgallocrecord2 |  | fmfgallocbillno |
| 2 | pk_sco_mfgallocrecord |  | fid |
| 3 | idx_sco_mfgallocrecord |  | forgid |

---

## 分配结果-子表 t_sco_mfgallocrecordentry

- **表名称：** 分配结果-子表
- **表名：** t_sco_mfgallocrecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbenefitcostcenterid | 受益成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fmfgfeestdbillno | 制造费用分配标准单据编码 | varchar | 255 |  | √ | ' ' | 制造费用分配标准单据编码 |
| 5 | fstdvalue | 分配标准值 | numeric | 23 | 10 | √ | 0 | 分配标准值 |
| 6 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_mfgallocrecordentry |  | fentryid |
| 2 | idx_sco_mfgallocrecordentry |  | fid,fbenefitcostcenterid |

---

## 子单据体-子表 t_sco_mfgallocrecordsub

- **表名称：** 子单据体-子表
- **表名：** t_sco_mfgallocrecordsub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbenefitcostcenterid | 受益成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fmfgfeestdbillno | 制造费用分配标准单据编码 | varchar | 255 |  | √ | ' ' | 制造费用分配标准单据编码 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fstdvalue | 分配标准值 | numeric | 23 | 10 | √ | 0 | 分配标准值 |
| 6 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_mfgallocrecordsub |  | fdetailid |
| 2 | idx_sco_mfgallocrecordsub |  | fentryid,fbenefitcostcenterid |
