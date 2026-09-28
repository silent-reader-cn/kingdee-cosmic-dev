# 市场数据主页设置-md_apphome_setting

## 市场数据主页设置-主表 t_md_apphome_setting

- **表名称：** 市场数据主页设置-主表
- **表名：** t_md_apphome_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatetype | 时间范围 | varchar | 50 |  | √ | ' ' | 时间范围,枚举: 7d :近一周 1m :近一月 3m :近三月 6m :近半年 1y :近一年 define :自定义 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fforexquoteid | 外汇报价 | int8 | 64 |  | √ | 0 | [外汇报价 md_forexquote_f7](../md_files/md_forexquote_f7.md) |
| 5 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbegindate | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 8 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fenddate | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | ftype | 设置类型 | varchar | 50 |  | √ | ' ' | 设置类型,枚举: forex :外汇 index :参考指数 yield :收益率曲线 |
| 15 | freferindexid | 参考利率 | int8 | 64 |  | √ | 0 | [参考利率表 tbd_referrate](../fbd_files/tbd_referrate.md) |
| 16 | fyieldcurveid | 收益率曲线 | int8 | 64 |  | √ | 0 | [收益率曲线 md_yieldcurve_f7](../md_files/md_yieldcurve_f7.md) |
| 17 | fenable | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | fcurrencypair | 货币对 | varchar | 50 |  | √ | ' ' | 货币对 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_md_apphome_setting_bb |  | fnumber |
| 2 | pk_t_md_apphome_setting |  | fid |

---

## 市场数据主页设置-多语言表 t_md_apphome_setting_l

- **表名称：** 市场数据主页设置-多语言表
- **表名：** t_md_apphome_setting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_apphome_setting_l |  | fpkid |
| 2 | idx_t_md_apphome_setting_l_bb |  | fid,flocaleid |
