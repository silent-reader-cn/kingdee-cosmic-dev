# B2B商城微页面配置-ocrpos_lightpageset

## 发布组件类型明细-多语言表 t_ocrpos_ltpageset_p_l

- **表名称：** 发布组件类型明细-多语言表
- **表名：** t_ocrpos_ltpageset_p_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fshopwindow | 橱窗名称 | varchar | 80 |  | √ | ' ' | 橱窗名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocrpos_ltpageset_p_l |  | fpkid |
| 2 | idx_ocrpos_ltpageset_p_l |  | fentryid |

---

## 组件类型明细-多语言表 t_ocrpos_ltpageset_e_l

- **表名称：** 组件类型明细-多语言表
- **表名：** t_ocrpos_ltpageset_e_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fshopwindow | 橱窗名称 | varchar | 80 |  | √ | ' ' | 橱窗名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocrpos_ltpageset_e_l |  | fentryid |
| 2 | pk_ocrpos_ltpageset_e_l |  | fpkid |

---

## 发布组件类型明细-子表 t_ocrpos_ltpageset_p

- **表名称：** 发布组件类型明细-子表
- **表名：** t_ocrpos_ltpageset_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fshopwindowseq | 橱窗序号 | int4 | 32 |  | √ | 0 | 橱窗序号 |
| 3 | fmoduledata | 组件配置数据 | varchar | 255 |  | √ | ' ' | 组件配置数据 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fmoduletypeid | 组件类型 | int8 | 64 |  | √ | 0 | [商城组件类型 ocrpos_moduletype](../ocrpos_files/ocrpos_moduletype.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fshopwindow | 橱窗名称 | varchar | 100 |  | √ | ' ' | 橱窗名称 |
| 8 | fmoduledata_tag | 组件配置数据_详情 | text | 0 |  |  | ' ' | 组件配置数据_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocrpos_ltpageset_p |  | fentryid |
| 2 | idx_ocrpos_ltpageset_p |  | fid |

---

## B2B商城微页面配置-多语言表 t_ocrpos_ltpageset_l

- **表名称：** B2B商城微页面配置-多语言表
- **表名：** t_ocrpos_ltpageset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 微页面名称 | varchar | 80 |  | √ | ' ' | 微页面名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocrpos_ltpageset_l |  | fpkid |
| 2 | idx_ocrpos_ltpageset_l |  | fid |

---

## B2B商城微页面配置-主表 t_ocrpos_ltpageset

- **表名称：** B2B商城微页面配置-主表
- **表名：** t_ocrpos_ltpageset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 微页面名称 | varchar | 80 |  | √ | ' ' | 微页面名称 |
| 3 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 唯一编码 | varchar | 80 |  | √ | ' ' | 唯一编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocrpos_ltpageset_num |  | fnumber |
| 2 | pk_ocrpos_ltpageset |  | fid |

---

## 组件类型明细-子表 t_ocrpos_ltpageset_e

- **表名称：** 组件类型明细-子表
- **表名：** t_ocrpos_ltpageset_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 3 | fmoduledata | 组件配置数据 | varchar | 255 |  | √ | ' ' | 组件配置数据 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fmoduletypeid | 组件类型 | int8 | 64 |  | √ | 0 | [商城组件类型 ocrpos_moduletype](../ocrpos_files/ocrpos_moduletype.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fshopwindow | 橱窗名称 | varchar | 100 |  | √ | ' ' | 橱窗名称 |
| 8 | fmoduledata_tag | 组件配置数据_详情 | text | 0 |  |  | ' ' | 组件配置数据_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocrpos_ltpageset_e |  | fentryid |
| 2 | idx_ocrpos_ltpageset_e |  | fid |
