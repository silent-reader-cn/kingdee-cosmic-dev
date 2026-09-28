# 合法性检查项-cad_checkitem

## 合法性检查项-主表 t_cad_checkitem

- **表名称：** 合法性检查项-主表
- **表名：** t_cad_checkitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 合法性检查项 | varchar | 1000 |  | √ | ' ' | 合法性检查项 |
| 3 | fopsuggestion | 操作建议 | varchar | 2000 |  | √ | ' ' | 操作建议 |
| 4 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 5 | fappnum | 所属应用 | varchar | 30 |  | √ | 'sca' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 6 | fispreset | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设 |
| 7 | fcustomfilter | 后台过滤条件（不可见） | varchar | 2000 |  | √ | ' ' | 后台过滤条件（不可见） |
| 8 | fbizobjectid | 业务对象 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fcustomfilter_tag | 后台过滤条件（不可见）_详情 | text | 0 |  |  | ' ' | 后台过滤条件（不可见）_详情 |
| 10 | fcheckmode | 检查项方式 | bpchar | 1 |  | √ | 'A' | 检查项方式,枚举: A :插件 B :自定义 |
| 11 | ferrorlog | 错误日志 | varchar | 2000 |  | √ | ' ' | 错误日志 |
| 12 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 13 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 14 | fcustomfiltertext | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_checkitem |  | fid |
| 2 | idx_cad_checkitem_num |  | fnumber |
| 3 | idx_cad_checkitem_app |  | fappnum |

---

## 合法性检查项-多语言表 t_cad_checkitem_l

- **表名称：** 合法性检查项-多语言表
- **表名：** t_cad_checkitem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 合法性检查项 | varchar | 1000 |  | √ | ' ' | 合法性检查项 |
| 3 | fopsuggestion | 操作建议 | varchar | 2000 |  | √ | ' ' | 操作建议 |
| 4 | ferrorlog | 错误日志 | varchar | 2000 |  | √ | ' ' | 错误日志 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 7 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_checkitem_l |  | fpkid |
| 2 | idx_cad_checkitem_l |  | fid,flocaleid |
