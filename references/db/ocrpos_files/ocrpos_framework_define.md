# 商城框架模板-ocrpos_framework_define

## 商城框架模板-主表 t_ocrpos_fx_define

- **表名称：** 商城框架模板-主表
- **表名：** t_ocrpos_fx_define

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fthemenumber | 主题编码 | varchar | 80 |  | √ | ' ' | 主题编码 |
| 3 | fname | 模板名称 | varchar | 80 |  | √ | ' ' | 模板名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fentityobjectid | 绑定页面对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fmalllogo | 商城Logo | varchar | 255 |  | √ | ' ' | 商城Logo |
| 13 | fuithemeid | 主题定制 | int8 | 64 |  | √ | 0 | 主题定制 bas_uitheme |
| 14 | fenable | 启用状态 | bpchar | 1 |  | √ | '0' | 启用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fthemename | 主题名称 | varchar | 80 |  | √ | ' ' | 主题名称 |
| 16 | fnumber | 模板编码 | varchar | 80 |  | √ | ' ' | 模板编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocrpos_fx_define_num |  | fnumber |
| 2 | pk_ocrpos_fx_define |  | fid |

---

## 商城框架模板-多语言表 t_ocrpos_fx_define_l

- **表名称：** 商城框架模板-多语言表
- **表名：** t_ocrpos_fx_define_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模板名称 | varchar | 80 |  | √ | ' ' | 模板名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocrpos_fx_define_l |  | fpkid |
| 2 | idx_ocrpos_fx_define_l |  | fid |
