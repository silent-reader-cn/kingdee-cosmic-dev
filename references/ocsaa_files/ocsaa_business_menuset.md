# 渠道管家(移动)菜单设置-ocsaa_business_menuset

## 自定义参数单据体-子表 t_ocsaa_bmenuset_params

- **表名称：** 自定义参数单据体-子表
- **表名：** t_ocsaa_bmenuset_params

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparamvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fparamkey | 参数Key | varchar | 50 |  | √ | ' ' | 参数Key |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocsaa_bmenuset_params |  | fentryid |
| 2 | idx_ocsaa_bmenuset_params |  | fid |

---

## 渠道管家(移动)菜单设置-多语言表 t_ocsaa_businessmenuset_l

- **表名称：** 渠道管家(移动)菜单设置-多语言表
- **表名：** t_ocsaa_businessmenuset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 5 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocsaa_businessmenuset_l |  | fpkid |
| 2 | idx_ocsaa_businessmenuset_l |  | fid,flocaleid |

---

## 渠道管家(移动)菜单设置-主表 t_ocsaa_businessmenuset

- **表名称：** 渠道管家(移动)菜单设置-主表
- **表名：** t_ocsaa_businessmenuset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 5 | fnavmenu | 底部导航菜单 | varchar | 80 |  | √ | ' ' | 底部导航菜单,枚举: channel :渠道 |
| 6 | fparentid | 上级 | int8 | 64 |  | √ | 0 | 渠道管家(移动)菜单设置 ocsaa_business_menuset |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | findex | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 9 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 13 | ficon | 图标 | varchar | 255 |  | √ | ' ' | 图标 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fopentype | 打开方式 | bpchar | 1 |  | √ | 'A' | 打开方式,枚举: A :打开新页面 B :打开页面底部导航 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fdesc | 描述 | varchar | 250 |  | √ | ' ' | 描述 |
| 20 | fformid | 表单 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocsaa_businessmenuset |  | fid |
| 2 | idx_ocsaa_busmenuset_parent |  | fparentid |
