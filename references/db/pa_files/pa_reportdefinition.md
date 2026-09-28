# 报表定义-pa_reportdefinition

## 报表定义-主表 t_pa_reportdefinition

- **表名称：** 报表定义-主表
- **表名：** t_pa_reportdefinition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fpublishtime | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 9 | fanalysis_model | 分析模型 | int8 | 64 |  | √ | 0 | [分析模型 pa_analysismodel](../pa_files/pa_analysismodel.md) |
| 10 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_reportdefinition_1 |  | fanalysis_model |
| 2 | pk_pa_reportdefinition |  | fid |
| 3 | idx_reportdefinition_2 |  | fnumber |

---

## 度量-多选基础资料表 t_pa_reportmeasuresconfig

- **表名称：** 度量-多选基础资料表
- **表名：** t_pa_reportmeasuresconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [度量 pa_measure](../pa_files/pa_measure.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_reportmeasuresconfig_1 |  | fentryid,fbasedataid |
| 2 | pk_pa_reportmeasuresconfig |  | fpkid |

---

## 权限用户-多选基础资料表 t_pa_reportpermuser

- **表名称：** 权限用户-多选基础资料表
- **表名：** t_pa_reportpermuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pa_reportpermuser |  | fpkid |
| 2 | idx_reportpermuser_1 |  | fid,fbasedataid |

---

## 报表定义-多语言表 t_pa_reportdefinition_l

- **表名称：** 报表定义-多语言表
- **表名：** t_pa_reportdefinition_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_reportdefinition_l_1 |  | fid |
| 2 | pk_pa_reportdefinition_l |  | fpkid |

---

## 行维度-子表 t_pa_rowentryconfig

- **表名称：** 行维度-子表
- **表名：** t_pa_rowentryconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | freportitem | 报表项目 | int8 | 64 |  | √ | 0 | [报表项目 pa_reportitem](../pa_files/pa_reportitem.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pa_rowentryconfig |  | fentryid |
| 2 | idx_rowentryconfig_2 |  | fid |
| 3 | idx_rowentryconfig_1 |  | freportitem |

---

## 列维度-子表 t_pa_columnentryconfig

- **表名称：** 列维度-子表
- **表名：** t_pa_columnentryconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmembername | 成员值范围 | varchar | 255 |  | √ | ' ' | 成员值范围 |
| 3 | fmemberid | 成员值ID | varchar | 255 |  | √ | ' ' | 成员值ID |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fmembernumber | 成员值范围编码 | varchar | 255 |  | √ | ' ' | 成员值范围编码 |
| 6 | fmembernameencode | 成员值范围转码 | varchar | 255 |  | √ | ' ' | 成员值范围转码 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fdimension | 维度 | int8 | 64 |  | √ | 0 | [维度 pa_dimension](../pa_files/pa_dimension.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_columnentryconfig_1 |  | fdimension |
| 2 | pk_pa_columnentryconfig |  | fentryid |
| 3 | idx_columnentryconfig_2 |  | fid |

---

## 度量设置-子表 t_pa_measureentryconfig

- **表名称：** 度量设置-子表
- **表名：** t_pa_measureentryconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fshoworder | 展示顺序 | bpchar | 1 |  | √ | '1' | 展示顺序,枚举: 0 :维度之前 1 :维度之后 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pa_measureentryconfig |  | fentryid |
| 2 | idx_measureentryconfig_1 |  | fid |

---

## 权限角色-多选基础资料表 t_pa_reportpermrole

- **表名称：** 权限角色-多选基础资料表
- **表名：** t_pa_reportpermrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pa_reportpermrole |  | fpkid |
| 2 | idx_reportpermrole_1 |  | fid,fbasedataid |
