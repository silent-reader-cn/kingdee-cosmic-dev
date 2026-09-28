# 卡片模板-pbd_cardtpl

## 卡片模板-主表 t_pbd_cardtpl

- **表名称：** 卡片模板-主表
- **表名：** t_pbd_cardtpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [卡片模板分组 pbd_cardtpl_group](../pbd_files/pbd_cardtpl_group.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcardid | 展示卡片 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 7 | fexampletpl_tag | 示例模板_详情 | text | 0 |  |  | null | 示例模板_详情 |
| 8 | fexampletpl | 示例模板 | varchar | 1000 |  | √ | ' ' | 示例模板 |
| 9 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fplugin | 模板解析插件 | varchar | 255 |  | √ | ' ' | 模板解析插件 |
| 16 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_cardtpl_fnum |  | fnumber |
| 2 | pk_pbd_cardtpl |  | fid |

---

## 配置项-子表 t_pbd_cardtplentry

- **表名称：** 配置项-子表
- **表名：** t_pbd_cardtplentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foptionaltype | 可选项类型 | bpchar | 1 |  | √ | ' ' | 可选项类型,枚举: 2 :数据绑定 3 :枚举 |
| 3 | foptionalconfig | 可选项配置 | varchar | 2000 |  | √ | ' ' | 可选项配置 |
| 4 | foptionitemkey | 配置项标识 | varchar | 80 |  | √ | ' ' | 配置项标识 |
| 5 | fisarray | 是否多值 | bpchar | 1 |  | √ | ' ' | 是否多值 |
| 6 | fdefaultvalue | 默认值 | varchar | 1000 |  | √ | ' ' | 默认值 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 9 | foptionitemname | foptionitemname | varchar | 80 |  | √ | ' ' |  |
| 10 | foptionitemtype | 配置项类型 | varchar | 30 |  | √ | ' ' | 配置项类型,枚举: string :字符串 integer :整数 decimal :小数 boolean :是/否 STRUCT :结构 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_cardtplentry |  | fentryid |
| 2 | idx_pbd_cardtplentry_fid |  | fid |

---

## 卡片模板-多语言表 t_pbd_cardtpl_l

- **表名称：** 卡片模板-多语言表
- **表名：** t_pbd_cardtpl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_cardtpl_l_fid |  | fid,flocaleid |
| 2 | pk_pbd_cardtpl_l |  | fpkid |
