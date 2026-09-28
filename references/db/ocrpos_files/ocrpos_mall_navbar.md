# B2B商城导航设置-ocrpos_mall_navbar

## B2B商城导航设置-主表 t_ocrpos_navbar

- **表名称：** B2B商城导航设置-主表
- **表名：** t_ocrpos_navbar

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 5 | fpagetype | 页面类型 | bpchar | 1 |  | √ | 'A' | 页面类型,枚举: A :微页面 B :元数据 C :链接 |
| 6 | fparentid | 上级导航 | int8 | 64 |  | √ | 0 | B2B商城导航设置 ocrpos_mall_navbar |
| 7 | flightpageid | 微页面 | int8 | 64 |  | √ | 0 | B2B商城微页面配置 ocrpos_lightpageset |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | flongnumber | 长编码 | varchar | 80 |  | √ | ' ' | 长编码 |
| 10 | fentityobjectid | 元数据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 11 | fframeworkdefineid | 商城模板 | int8 | 64 |  | √ | 0 | 商城框架模板 ocrpos_framework_define |
| 12 | fshowseq | 显示顺序 | int4 | 32 |  | √ | 0 | 显示顺序 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fopenlink | 链接 | varchar | 255 |  | √ | ' ' | 链接 |
| 15 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fshowmodel | 显示模式 | bpchar | 1 |  | √ | 'A' | 显示模式,枚举: A :表单 B :列表 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 22 | fshowtype | 显示方式 | bpchar | 1 |  | √ | 'A' | 显示方式,枚举: A :新页签 B :弹窗 C :内嵌(当前页) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocrpos_navbar |  | fid |
| 2 | idx_ocrpos_navbar_num |  | fnumber |

---

## 自定义参数单据体-子表 t_ocrpos_navbar_p

- **表名称：** 自定义参数单据体-子表
- **表名：** t_ocrpos_navbar_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparamvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 3 | fparamname | 参数名 | varchar | 80 |  | √ | ' ' | 参数名 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocrpos_navbar_p |  | fentryid |
| 2 | idx_ocrpos_navbar_p |  | fid |

---

## B2B商城导航设置-多语言表 t_ocrpos_navbar_l

- **表名称：** B2B商城导航设置-多语言表
- **表名：** t_ocrpos_navbar_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocrpos_navbar_l |  | fpkid |
| 2 | idx_ocrpos_navbar_l |  | fid |
