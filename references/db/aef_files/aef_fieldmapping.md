# 归档字段配置-aef_fieldmapping

## 归档字段配置-多语言表 t_aef_fieldmapping_l

- **表名称：** 归档字段配置-多语言表
- **表名：** t_aef_fieldmapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aef_fieldmapping_l |  | fpkid |
| 2 | idx_aef_fieldmapping_l |  | fid,flocaleid |

---

## 单据体-子表 t_aef_mappingentry

- **表名称：** 单据体-子表
- **表名：** t_aef_mappingentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldnumber | 字段标识 | varchar | 200 |  |  | ' ' | 字段标识 |
| 3 | fxmlfiled | 档案字段标识 | varchar | 200 |  | √ | ' ' | 档案字段标识 |
| 4 | ffieldtype | 字段类型 | bpchar | 1 |  | √ | ' ' | 字段类型,枚举: 1 :文本 2 :金额 3 :基础资料 4 :复选框 5 :日期 |
| 5 | ffieldname | 字段名称 | varchar | 200 |  | √ | ' ' | 字段名称 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdisplayprop | 基础资料归档属性 | bpchar | 1 |  | √ | ' ' | 基础资料归档属性,枚举: 1 :编码 2 :名称 3 :编码+名称 |
| 8 | fissyspreset | 是否预置 | bpchar | 1 |  | √ | ' ' | 是否预置 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aef_mappingentry_fid |  | fid |
| 2 | pk_t_aef_mappingentry |  | fentryid |

---

## 归档字段配置-主表 t_aef_fieldmapping

- **表名称：** 归档字段配置-主表
- **表名：** t_aef_fieldmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | ffielddisplay | 列表展示字段 | varchar | 200 |  | √ | ' ' | 列表展示字段 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fserviceid | 适用档案系统 | int8 | 64 |  | √ | 0 | [归档服务器配置 aef_serviceconfig](../aef_files/aef_serviceconfig.md) |
| 12 | fxmlnode | xml节点名称 | varchar | 200 |  | √ | ' ' | xml节点名称 |
| 13 | fnumber | 编码 | varchar | 200 |  | √ | ' ' | 编码 |
| 14 | fbilltype | 单据类型 | varchar | 60 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aef_fieldmapping |  | fid |
| 2 | idx_aef_fieldmapping |  | fnumber |
