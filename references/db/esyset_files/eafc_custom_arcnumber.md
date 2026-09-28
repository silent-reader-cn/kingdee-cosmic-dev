# 编号规则配置-eafc_custom_arcnumber

## 适用分类-多选基础资料表 tk_eafc_syset_busf7_mult

- **表名称：** 适用分类-多选基础资料表
- **表名：** tk_eafc_syset_busf7_mult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_syset_busf7_mult |  | fpkid |

---

## 单据体-子表 tk_eafc_custom_arcnum_ent

- **表名称：** 单据体-子表
- **表名：** tk_eafc_custom_arcnum_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_eafc_splitsign | 段间分隔符 | varchar | 50 |  | √ | ' ' | 段间分隔符,枚举: 1 :- 2 :@ 3 :# 4 :$ 5 :% 6 :^ 7 :& 8 :* 9 :[ 10 :] 11 :· 12 :_ |
| 3 | fk_eafc_length | 长度 | int4 | 32 |  | √ | 0 | 长度 |
| 4 | fk_eafc_labelapnum | 文本5 | varchar | 50 |  | √ | ' ' | 文本5 |
| 5 | fk_eafc_format | 显示格式 | varchar | 50 |  | √ | ' ' | 显示格式 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fk_fpy_num_fix | 数字格式 | varchar | 50 |  | √ | ' ' | 数字格式,枚举: 1 :x 2 :xx |
| 8 | fk_eafc_attributetype | 属性类型 | varchar | 50 |  | √ | ' ' | 属性类型,枚举: 1 :预置字段 2 :随机码 3 :系统日期 4 :流水号 5 :业务对象字段 6 :业务对象日期 7 :常量 |
| 9 | fk_eafc_fixval | 设置值(数据) | varchar | 200 |  | √ | ' ' | 设置值(数据) |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fk_eafc_serialbasis | 流水号依据 | varchar | 50 |  | √ | ' ' | 流水号依据,枚举: 1 :设为依据 2 :设为依据 4 :非依据 3 :设为依据不显示 |
| 12 | fk_eafc_initial | 起始值 | int4 | 32 |  | √ | 0 | 起始值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_custom_arcnum_ent |  | fentryid |

---

## 编号规则配置-多语言表 tk_eafc_custom_arcnumber_l

- **表名称：** 编号规则配置-多语言表
- **表名：** tk_eafc_custom_arcnumber_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 50 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_custom_arcnumber_l |  | fpkid |

---

## 编号规则配置-主表 tk_eafc_custom_arcnumber

- **表名称：** 编号规则配置-主表
- **表名：** tk_eafc_custom_arcnumber

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 规则名称 | varchar | 50 |  | √ | ' ' | 规则名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fk_eafc_is_modify | 是否可修改 | bpchar | 1 |  | √ | '0' | 是否可修改 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fk_eafc_control_scheme | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 1 :全局共享 2 :私有 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fk_eafc_custom_numtree | 规则对象 | int8 | 64 |  |  | null | [自定义编号树形类型维护 eafc_custom_numtree](../esyset_files/eafc_custom_numtree.md) |
| 10 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fk_eafc_example | 编码示例 | varchar | 50 |  | √ | ' ' | 编码示例 |
| 13 | fenable | 启用状态 | varchar | 50 |  | √ | ' ' | 启用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fk_eafc_textfield | 文本1 | varchar | 200 |  | √ | ' ' | 文本1 |
| 15 | fnumber | 规则编码 | varchar | 30 |  | √ | ' ' | 规则编码 |
| 16 | fk_eafc_business | 适用分类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 17 | fk_eafc_arcorg | 创建组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_custom_arcnumber |  | fid |
