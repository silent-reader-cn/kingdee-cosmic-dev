# 全局数据规则控制表单-perm_overallprop_rel

## 单据体_例外角色-子表 t_perm_ovralldr_exprole

- **表名称：** 单据体_例外角色-子表
- **表名：** t_perm_ovralldr_exprole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | froleid | 角色编码 | varchar | 36 |  | √ | ' ' | 通用角色 perm_role |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_ovralldr_exprole |  | fentryid |
| 2 | idx_perm_ovralldr_exprole_fk |  | fid |

---

## 子单据体-子表 t_perm_ovrallpropreldet

- **表名称：** 子单据体-子表
- **表名：** t_perm_ovrallpropreldet

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubdimensiontype | 维度属性 | varchar | 36 |  | √ | ' ' | 全局数据规则控制维度 perm_overallprop |
| 2 | fsubpropentnum | 基础资料类型 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 3 | fsubfieldtype | 属性类型 | varchar | 50 |  | √ | ' ' | 属性类型,枚举: BasedataProp :基础资料 TextProp :文本 ComboProp :下拉列表 |
| 4 | fsubpropkey | 属性名称 | varchar | 50 |  | √ | ' ' | 属性名称,枚举: |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | null | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_ovrallpropreldet |  | fdetailid |
| 2 | idx_perm_ovrallpropreldet_fk |  | fentryid |

---

## 全局数据规则控制表单-主表 t_perm_overallproprel

- **表名称：** 全局数据规则控制表单-主表
- **表名：** t_perm_overallproprel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentitynum | 业务对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | foverallprop | foverallprop | int8 | 64 |  | √ | 0 |  |
| 4 | fapplyscope | fapplyscope | bpchar | 1 |  | √ | '1' |  |
| 5 | fpropkey | fpropkey | varchar | 36 |  | √ | ' ' |  |
| 6 | fappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_overallproprel |  | fappid,fentitynum |
| 2 | pk_t_perm_overallproprel |  | fid |

---

## 单据体_主属性-子表 t_perm_ovrallproprelentry

- **表名称：** 单据体_主属性-子表
- **表名：** t_perm_ovrallproprelentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fpropkey | 属性名称 | varchar | 30 |  | √ | ' ' | 属性名称,枚举: |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_perm_ovrallproprelentry |  | fentryid |
| 2 | idx_perm_ovrallproprelentry |  | fid |

---

## 单据体_角色控制规则-子表 t_perm_ovralldr_rolectrl

- **表名称：** 单据体_角色控制规则-子表
- **表名：** t_perm_ovralldr_rolectrl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | froleid | 角色编码 | varchar | 36 |  | √ | ' ' | 通用角色 perm_role |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_ovralldr_rolectrl |  | fentryid |
| 2 | idx_perm_ovralldr_rolectrl_fk |  | fid |
