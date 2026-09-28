# 资料形式（三级类别）-eafc_business_type

## 资料形式（三级类别）-多语言表 tk_eafc_business_type_l

- **表名称：** 资料形式（三级类别）-多语言表
- **表名：** tk_eafc_business_type_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
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
| 1 | pk_eafc_business_type_l |  | fpkid |
| 2 | idx_eafc_business_type_l_fk |  | fid |

---

## 资料形式（三级类别）-主表 tk_eafc_business_type

- **表名称：** 资料形式（三级类别）-主表
- **表名：** tk_eafc_business_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_businesstype | 业务类型枚举 | int8 | 64 |  |  | null | 业务类型枚举 |
| 3 | fk_eafc_fis_system | 是否系统预制 | varchar | 50 |  | √ | ' ' | 是否系统预制,枚举: 1 :是 2 :否 |
| 4 | fk_eafc_businesscode | 业务代码 | varchar | 50 |  | √ | ' ' | 业务代码 |
| 5 | fk_eafc_fcategory_code | 三级类别号 | varchar | 50 |  | √ | ' ' | 三级类别号 |
| 6 | fk_fpy_layout_volume | 案卷布局界面 | varchar | 50 |  | √ | ' ' | 案卷布局界面 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 11 | fk_eafc_billid | 对应表单id | varchar | 50 |  | √ | ' ' | 对应表单id |
| 12 | fk_eafc_businessname | 类别号描述 | varchar | 50 |  | √ | ' ' | 类别号描述 |
| 13 | fk_fpy_layout_file | 整理布局界面 | varchar | 50 |  | √ | ' ' | 整理布局界面 |
| 14 | fk_eafc_fuseing | 是否在用 | varchar | 50 |  | √ | ' ' | 是否在用,枚举: 1 :是 2 :否 |
| 15 | fk_eafc_storage_period | 保管期限 | varchar | 50 |  | √ | ' ' | 保管期限,枚举: 1 :10年 2 :30年 3 :永久 |
| 16 | fk_eafc_identification | 业务类型标识 | varchar | 50 |  | √ | ' ' | 业务类型标识 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 19 | fk_fpy_layout_pre | 预归档布局界面 | varchar | 50 |  | √ | ' ' | 预归档布局界面 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fk_eafc_manager_type | 单选按钮组 | varchar | 50 |  | √ | ' ' | 单选按钮组,枚举: 1 :按卷整理 2 :按件整理 |
| 22 | fk_fpy_im_template | 集成平台模板 | varchar | 50 |  | √ | ' ' | 集成平台模板 |
| 23 | fk_fpy_layout_cateview | 离线采集页面 | varchar | 50 |  | √ | ' ' | 离线采集页面 |
| 24 | fk_fpy_layout_report | 报表布局界面 | varchar | 50 |  | √ | ' ' | 报表布局界面 |
| 25 | fk_eafc_combofield | 组件位制 | varchar | 50 |  | √ | ' ' | 组件位制,枚举: 1 :万位 2 :十万位 3 :百万位 4 :千万位 5 :亿位 |
| 26 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fk_eafc_archive | 一级类别号 | int8 | 64 |  |  | null | [档案类型（一级） eafc_archive_type](../ebase_files/eafc_archive_type.md) |
| 28 | fk_eafc_category | 所属门类(二级) | int8 | 64 |  |  | null | [档案门类（二级） eafc_category](../ebase_files/eafc_category.md) |
| 29 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_business_type |  | fid |

---

## 关系配置-子表 tk_fpy_rel_entryentity

- **表名称：** 关系配置-子表
- **表名：** tk_fpy_rel_entryentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_fpy_rel_combo | 关系类型 | varchar | 50 |  | √ | ' ' | 关系类型,枚举: 1 :直接关系 |
| 3 | fk_fpy_category_son | 子分类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_rel_entryentity |  | fentryid |
