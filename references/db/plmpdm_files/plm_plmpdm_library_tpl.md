# 库模板-plm_plmpdm_library_tpl

## 库模板-多语言表 t_plmpdm_library_tpl_l

- **表名称：** 库模板-多语言表
- **表名：** t_plmpdm_library_tpl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模板名称 | varchar | 399 |  | √ | ' ' | 模板名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmpdm_library_tpl_l |  | fpkid |
| 2 | idx_plmpdm_library_tpl_0 |  | fid,flocaleid |

---

## 库模板-主表 t_plmpdm_library_tpl

- **表名称：** 库模板-主表
- **表名：** t_plmpdm_library_tpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 模板名称 | varchar | 255 |  | √ | ' ' | 模板名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | flibtemplatetype | 库模板类型 | bpchar | 1 |  | √ | 'A' | 库模板类型,枚举: A :产品库模板 B :资源库模板 C :配置库模版 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcontent_tag | 大文本_详情 | text | 0 |  |  | null | 大文本_详情 |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 14 | fcontent | 大文本 | varchar | 255 |  | √ | ' ' | 大文本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmpdm_library_tpl_m0 |  | fname |
| 2 | pk_plmpdm_library_tpl |  | fid |
