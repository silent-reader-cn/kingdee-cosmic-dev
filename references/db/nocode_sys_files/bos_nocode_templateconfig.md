# 模板配置-bos_nocode_templateconfig

## 模板配置-主表 t_nocode_template_config

- **表名称：** 模板配置-主表
- **表名：** t_nocode_template_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffrequency | 使用次数 | int8 | 64 |  | √ | 0 | 使用次数 |
| 3 | fname | 模板名称 | varchar | 50 |  | √ | ' ' | 模板名称 |
| 4 | ftag | 标签 | varchar | 500 |  | √ | ' ' | 标签 |
| 5 | fsourceid | 模板来源 | varchar | 50 |  | √ | ' ' | 模板来源 |
| 6 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | forg | 组织 | varchar | 50 |  | √ | ' ' | 组织 |
| 8 | fappid | 应用id | varchar | 50 |  | √ | ' ' | 应用id |
| 9 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | ficon | 图标 | varchar | 200 |  | √ | ' ' | 图标 |
| 11 | ftype | 下拉列表 | varchar | 50 |  | √ | ' ' | 下拉列表,枚举: 0 :表单模板 1 :应用模板 |
| 12 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 13 | fimage | 图片 | varchar | 200 |  | √ | ' ' | 图片 |
| 14 | fformid | 模板表单id | varchar | 50 |  | √ | ' ' | 模板表单id |
| 15 | fview | 查看次数 | int8 | 64 |  | √ | 0 | 查看次数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_nc_tc_type |  | ftype |
| 2 | pk_nocode_template_config |  | fid |

---

## 行业-多选基础资料表 t_nocode_template_trade

- **表名称：** 行业-多选基础资料表
- **表名：** t_nocode_template_trade

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 模板行业 bos_nocode_ttrades |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_nocode_template_trade |  | fpkid |
| 2 | idx_nc_tt_fid |  | fid |

---

## 领域-多选基础资料表 t_nocode_template_domain

- **表名称：** 领域-多选基础资料表
- **表名：** t_nocode_template_domain

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 模板领域 bos_nocode_tdomains |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_nocode_template_domain |  | fpkid |
| 2 | idx_nc_td_ffid |  | fid |
