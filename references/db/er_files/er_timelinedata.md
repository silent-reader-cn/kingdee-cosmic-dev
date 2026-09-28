# 我的足迹中城市对应描述数据-er_timelinedata

## 我的足迹中城市对应描述数据-主表 t_er_timelinedata

- **表名称：** 我的足迹中城市对应描述数据-主表
- **表名：** t_er_timelinedata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fslogon | fslogon | varchar | 100 |  | √ | ' ' |  |
| 3 | furl | 城市图片链接 | varchar | 255 |  | √ | ' ' | 城市图片链接 |
| 4 | fcity | fcity | varchar | 100 |  | √ | ' ' |  |
| 5 | fpoem | fpoem | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_timelinedata_pkey |  | fid |
| 2 | idx_er_tild_fcity |  | fcity |

---

## 我的足迹中城市对应描述数据-多语言表 t_er_timelinedata_l

- **表名称：** 我的足迹中城市对应描述数据-多语言表
- **表名：** t_er_timelinedata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fslogon | 标语 | varchar | 100 |  | √ | ' ' | 标语 |
| 3 | fcity | 城市 | varchar | 100 |  | √ | ' ' | 城市 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpoem | 诗意 | varchar | 300 |  | √ | ' ' | 诗意 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_tld_l_id |  | fid,flocaleid |
| 2 | t_er_timelinedata_l_pkey |  | fpkid |
