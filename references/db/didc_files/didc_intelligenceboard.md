# AI看板-didc_intelligenceboard

## 角色权限-子表 t_didc_board_role

- **表名称：** 角色权限-子表
- **表名：** t_didc_board_role

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | froleid | 角色 | varchar | 36 |  | √ | ' ' | 通用角色 perm_role |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_board_role |  | fid |
| 2 | pk_t_didc_board_role |  | fentryid |

---

## 卡片单据体-多语言表 t_didc_cardentry_l

- **表名称：** 卡片单据体-多语言表
- **表名：** t_didc_cardentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcardname | 卡片名称 | varchar | 255 |  | √ | ' ' | 卡片名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_didc_cardentry_l |  | fpkid |
| 2 | idx_didc_cardentry_l |  | fentryid,flocaleid |

---

## AI看板-主表 t_didc_intelligenceboard

- **表名称：** AI看板-主表
- **表名：** t_didc_intelligenceboard

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 看板名称 | varchar | 255 |  | √ | ' ' | 看板名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ftheme | 看板主题 | varchar | 255 |  | √ | ' ' | 看板主题 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | flayout | 布局信息 | varchar | 255 |  | √ | ' ' | 布局信息 |
| 7 | flayout_tag | 布局信息_详情 | text | 0 |  |  | null | 布局信息_详情 |
| 8 | ffiltervalue | 全局过滤信息 | varchar | 255 |  | √ | ' ' | 全局过滤信息 |
| 9 | frole | 看板使用者 | varchar | 255 |  | √ | ' ' | 看板使用者 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatevalue_tag | 智能生成缓存_详情 | text | 0 |  |  | null | 智能生成缓存_详情 |
| 15 | fpreset | 是否预置 | bpchar | 1 |  | √ | ' ' | 是否预置 |
| 16 | ffiltervalue_tag | 全局过滤信息_详情 | text | 0 |  |  | null | 全局过滤信息_详情 |
| 17 | fcreatevalue | 智能生成缓存 | varchar | 255 |  | √ | ' ' | 智能生成缓存 |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_didc_intelligenceboard |  | fid |
| 2 | idx_didc_intelligenceboard |  | fnumber |

---

## 用户权限-子表 t_didc_board_user

- **表名称：** 用户权限-子表
- **表名：** t_didc_board_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuserfield | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_board_user |  | fid |
| 2 | pk_t_didc_board_user |  | fentryid |

---

## AI看板-多语言表 t_didc_intelligenceboard_l

- **表名称：** AI看板-多语言表
- **表名：** t_didc_intelligenceboard_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 看板名称 | varchar | 255 |  | √ | ' ' | 看板名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_didc_intelligenceboard_l |  | fpkid |
| 2 | idx_didc_intelligenceboard_l |  | fid,flocaleid |

---

## 卡片单据体-子表 t_didc_cardentry

- **表名称：** 卡片单据体-子表
- **表名：** t_didc_cardentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcardname | 卡片名称 | varchar | 255 |  | √ | ' ' | 卡片名称 |
| 3 | fconfig | 卡片参数 | varchar | 255 |  | √ | ' ' | 卡片参数 |
| 4 | fcardid | 卡片id | int8 | 64 |  | √ | 0 | 卡片id |
| 5 | fconfig_tag | 卡片参数_详情 | text | 0 |  |  | null | 卡片参数_详情 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fcardindex | 关联指标 | int8 | 64 |  | √ | 0 | 数智指标 didc_indexcatalogue |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_cardentry |  | fid |
| 2 | pk_t_didc_cardentry |  | fentryid |
