# 业务预警对象-warn_earlywarn

## 业务预警对象-多语言表 t_warn_earlywarn_l

- **表名称：** 业务预警对象-多语言表
- **表名：** t_warn_earlywarn_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdata | fdata | text | 0 |  |  | null |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_warn_earlywarn_l_pkey |  | fpkid |
| 2 | idx_warn_earlywarn_fid |  | fid,flocaleid |
| 3 | idx_warn_earlywarn_name |  | fname |

---

## 业务预警对象-主表 t_warn_earlywarn

- **表名称：** 业务预警对象-主表
- **表名：** t_warn_earlywarn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fparentid | ParentId | varchar | 36 |  | √ | ' ' | ParentId |
| 4 | fmodeltype | fmodeltype | varchar | 30 |  | √ | 'EarlyWarnModel' |  |
| 5 | fisv | 开发商 | varchar | 10 |  | √ | ' ' | 开发商 |
| 6 | fdatasourceid | 数据源 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fleaf | 叶子节点 | bpchar | 1 |  | √ | '1' | 叶子节点 |
| 8 | finheritpath | 继承路径 | varchar | 300 |  | √ | ' ' | 继承路径 |
| 9 | fbizappid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 10 | fdatasourcetype | 数据源类型 | varchar | 10 |  | √ | 'Custom' | 数据源类型,枚举: bill :单据 basedata :基础资料 report :报表 custom :自定义数据源 |
| 11 | fcreatedate | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 12 | ftype | 扩展状态 | bpchar | 1 |  | √ | '0' | 扩展状态,枚举: 0 :未扩展 1 :已继承 2 :已扩展 |
| 13 | fmasterid | 原始业务预警对象 | varchar | 36 |  | √ | ' ' | 原始业务预警对象 |
| 14 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 15 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 16 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
| 17 | fenabled | fenabled | bpchar | 1 |  | √ | '1' |  |
| 18 | fdata | fdata | text | 0 |  |  | null |  |
| 19 | ftimestamp | ftimestamp | int8 | 64 |  | √ | 0 |  |
| 20 | fistemplate | fistemplate | bpchar | 1 |  | √ | '0' |  |
| 21 | fconditionformid | 条件配置表单 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 22 | fversion | fversion | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_warn_earlywarn_fmasterid |  | fmasterid |
| 2 | t_warn_earlywarn_pkey |  | fid |
| 3 | idx_warn_earlywarn_fnumber |  | fnumber |
