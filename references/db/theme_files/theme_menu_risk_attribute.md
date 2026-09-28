# IPO主题分析菜单-风险标签属性-theme_menu_risk_attribute

## IPO主题分析菜单-风险标签属性-主表 t_theme_menu_risk_attribu

- **表名称：** IPO主题分析菜单-风险标签属性-主表
- **表名：** t_theme_menu_risk_attribu

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | IPO主题分析菜单类型 theme_menu_type |
| 5 | fbelongtoentryentity | 是否附属于单据体 | varchar | 50 |  | √ | ' ' | 是否附属于单据体,枚举: 1 :否 2 :是 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fentryentitytable | 单据体所属表名 | varchar | 50 |  | √ | ' ' | 单据体所属表名 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ftextfield | 具体指标区分值 | varchar | 50 |  | √ | ' ' | 具体指标区分值 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 字段标识 | varchar | 30 |  | √ | ' ' | 字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_menu_risk_attribu_name |  | fname |
| 2 | pk_theme_menu_risk_attribu |  | fid |

---

## IPO主题分析菜单-风险标签属性-多语言表 t_theme_menu_risk_attribu_l

- **表名称：** IPO主题分析菜单-风险标签属性-多语言表
- **表名：** t_theme_menu_risk_attribu_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
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
| 1 | pk_theme_menu_risk_attribu_l |  | fpkid |
| 2 | idx_menu_risk_attribu_lname |  | flocaleid,fname |
