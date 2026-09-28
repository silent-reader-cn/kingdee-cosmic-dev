# 检查项-cal_datacheck_item

## 检查项-主表 t_cal_datacheck_item

- **表名称：** 检查项-主表
- **表名：** t_cal_datacheck_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fbizobject | 业务对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fiserroritem | 数据错误项 | bpchar | 1 |  | √ | ' ' | 数据错误项 |
| 5 | fdescription | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |
| 6 | fappnum | 应用编码 | varchar | 10 |  | √ | ' ' | 应用编码 |
| 7 | ftips | 提示语 | varchar | 1000 |  | √ | ' ' | 提示语 |
| 8 | fispreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 9 | fcustomfilter | 后台过滤条件（不可见） | varchar | 255 |  | √ | ' ' | 后台过滤条件（不可见） |
| 10 | fexpmsgfields | 异常内容描述 | varchar | 255 |  | √ | ' ' | 异常内容描述,枚举: |
| 11 | fcustomfilter_tag | 后台过滤条件（不可见）_详情 | text | 0 |  |  | null | 后台过滤条件（不可见）_详情 |
| 12 | fcheckmode | 检查项方式 | varchar | 5 |  | √ | ' ' | 检查项方式,枚举: A :自定义 B :插件 |
| 13 | fplugin | 插件 | varchar | 225 |  | √ | ' ' | 插件 |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 15 | fcustomfiltertext | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_checkitem_no |  | fnumber |
| 2 | t_cal_datacheck_item_pkey |  | fid |

---

## 检查项-多语言表 t_cal_datacheck_item_l

- **表名称：** 检查项-多语言表
- **表名：** t_cal_datacheck_item_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 512 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | ftips | 提示语 | varchar | 1000 |  | √ | ' ' | 提示语 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_datacheck_item_l_pkey |  | fpkid |
| 2 | idx_cal_chitem_l_fid |  | fid |
