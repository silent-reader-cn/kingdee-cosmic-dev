# 首页卡片配置信息-bos_mainpagecardconfig

## 首页卡片配置信息-主表 t_bas_cardconfig

- **表名称：** 首页卡片配置信息-主表
- **表名：** t_bas_cardconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 卡片类型 | varchar | 36 |  | √ | ' ' | 卡片类型,枚举: 1 :快速发起 2 :单据统计 3 :工作流 4 :云之家订阅 5 :轻分析 |
| 3 | fconfig | 配置信息 | text | 0 |  |  | null | 配置信息 |
| 4 | fcardid | 卡片ID | int8 | 64 |  | √ | 0 | 卡片ID |
| 5 | fsourceid | 卡片池 | int8 | 64 |  | √ | 0 | 首页卡片 xkportal_card |
| 6 | fmainpageid | 首页布局 | int8 | 64 |  | √ | 0 | 首页方案 portal_scheme |
| 7 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bas_cardconfig_fuserid |  | fuserid |
| 2 | t_bas_cardconfig_pkey |  | fid |
| 3 | idx_cardconfig_fmainpageid |  | fmainpageid |
| 4 | idx_t_bas_cardconfig_fsourceid |  | fsourceid |

---

## 首页卡片配置信息-多语言表 t_bas_cardconfig_l

- **表名称：** 首页卡片配置信息-多语言表
- **表名：** t_bas_cardconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustomname | 自定义名称 | varchar | 500 |  | √ | ' ' | 自定义名称 |
| 3 | fcardtitle | 卡片标题 | varchar | 100 |  | √ | ' ' | 卡片标题 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bas_cardconfig_fid |  | fid,flocaleid |
| 2 | t_bas_cardconfig_l_pkey |  | fpkid |
