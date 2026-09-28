# 排序规则-ocdbd_ordersortrule

## 排序规则-主表 t_ocdbd_sortorder

- **表名称：** 排序规则-主表
- **表名：** t_ocdbd_sortorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcomment | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fschemeid | 智能审单方案 | int8 | 64 |  | √ | 0 | [智能审单方案 ocdbd_scheme](../ocdbd_files/ocdbd_scheme.md) |
| 7 | fispreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fexpeditortag | 公式表达式（后台大文本字段） | text | 0 |  |  | ' ' | 公式表达式（后台大文本字段） |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fbillcolname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 14 | fbillcol | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 15 | fbillid | 单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 18 | fexpeditortag_tag | 公式表达式（后台大文本字段）_详情 | text | 0 |  |  | ' ' | 公式表达式（后台大文本字段）_详情 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fsorttype | 排序类型 | bpchar | 1 |  | √ | ' ' | 排序类型,枚举: 1 :字段 2 :公式 3 :插件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_sortorder |  | fschemeid |
| 2 | pk_ocdbd_sortorder |  | fid |

---

## 排序规则-多语言表 t_ocdbd_sortorder_l

- **表名称：** 排序规则-多语言表
- **表名：** t_ocdbd_sortorder_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_sortorder_l |  | fid,flocaleid |
| 2 | pk_ocdbd_sortorder_l |  | fpkid |
