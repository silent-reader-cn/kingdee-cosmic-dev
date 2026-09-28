# 数据检查结果-sco_datacheckresult

## 异常对象-子表 t_sco_datacheckresultsub

- **表名称：** 异常对象-子表
- **表名：** t_sco_datacheckresultsub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fobjtypeid | 对象类型 | varchar | 255 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 2 | ffisrepaired | 是否已修复 | bpchar | 1 |  | √ | '0' | 是否已修复 |
| 3 | fobjid | 异常对象ID | int8 | 64 |  | √ | 0 | 异常对象ID |
| 4 | fextralinfo | 其它信息 | varchar | 255 |  | √ | ' ' | 其它信息 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fobjdes | 对象描述 | varchar | 255 |  | √ | ' ' | 对象描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_datacheckresultsub |  | fobjid,fobjtypeid |
| 2 | pk_sco_datacheckresultsub |  | fdetailid |

---

## 数据检查结果-主表 t_sco_datacheckresult

- **表名称：** 数据检查结果-主表
- **表名：** t_sco_datacheckresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: A :进行中 B :已完成 |
| 3 | fuserid | 检查用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sco :标准成本 aca :实际成本 |
| 5 | fchecktime | 检查日期 | timestamp | 0 |  |  | null | 检查日期 |
| 6 | fchecktaskid | 检查任务 | int8 | 64 |  | √ | 0 | [数据检查任务 sco_datachecktask](../sco_files/sco_datachecktask.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_datacheckresult |  | fid |
| 2 | idx_sco_datacheckresult |  | fchecktaskid,fuserid,fappnum |

---

## 检查详情-子表 t_sco_datacheckresulttry

- **表名称：** 检查详情-子表
- **表名：** t_sco_datacheckresulttry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrystatus | 检查结果 | varchar | 30 |  | √ | ' ' | 检查结果,枚举: A :警告 B :失败 C :异常 D :成功 E :部分修复 F :已修复 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fruningstatus | 运行状态 | varchar | 30 |  | √ | ' ' | 运行状态,枚举: A :未开始 B :运行中 C :已完成 |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fcheckitemid | 检查项 | int8 | 64 |  | √ | 0 | [数据检查项 sco_datacheckitem](../sco_files/sco_datacheckitem.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_datacheckresulttry |  | fcheckitemid |
| 2 | pk_sco_datacheckresulttry |  | fentryid |
