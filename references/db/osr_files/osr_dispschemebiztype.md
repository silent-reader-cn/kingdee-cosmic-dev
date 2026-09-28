# 界面显示方案业务类型-osr_dispschemebiztype

## 依赖许可单据体-多语言表 t_osr_dispschbiztype_p_l

- **表名称：** 依赖许可单据体-多语言表
- **表名：** t_osr_dispschbiztype_p_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flicensegroupname | 许可分组名称 | varchar | 240 |  | √ | ' ' | 许可分组名称 |
| 2 | fdeplicensemodulen | 依赖许可所属模块名称 | varchar | 240 |  | √ | ' ' | 依赖许可所属模块名称 |
| 3 | fdeplicensegroupn | 依赖许可分组名称 | varchar | 240 |  | √ | ' ' | 依赖许可分组名称 |
| 4 | flicensemodulename | 许可模块名称 | varchar | 240 |  | √ | ' ' | 许可模块名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_osr_dispschbiztype_p_l |  | fpkid |
| 2 | t_osr_dispschbiztype_p_l_idx |  | fentryid,flocaleid |

---

## 配置项单据体-多语言表 t_osr_dispschbiztype_c_l

- **表名称：** 配置项单据体-多语言表
- **表名：** t_osr_dispschbiztype_c_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftipstitle | 帮助提示标题 | varchar | 240 |  | √ | ' ' | 帮助提示标题 |
| 2 | fconfigname | 配置项名称 | varchar | 240 |  | √ | ' ' | 配置项名称 |
| 3 | fconfigdfvalue | 默认值 | varchar | 1200 |  | √ | ' ' | 默认值 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | ftipscontent | 帮助提示内容 | varchar | 600 |  | √ | ' ' | 帮助提示内容 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_dispschbiztype_c_l |  | fentryid,flocaleid |
| 2 | pk_t_osr_dispschbiztype_c_l |  | fpkid |

---

## 配置项单据体-子表 t_osr_dispschbiztype_c

- **表名称：** 配置项单据体-子表
- **表名：** t_osr_dispschbiztype_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftipstitle | 帮助提示标题 | varchar | 80 |  | √ | ' ' | 帮助提示标题 |
| 3 | fconfigkey | 配置项标识 | varchar | 80 |  | √ | ' ' | 配置项标识 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fconfigname | 配置项名称 | varchar | 80 |  | √ | ' ' | 配置项名称 |
| 6 | fconfigdfvalue | 默认值 | varchar | 500 |  | √ | ' ' | 默认值 |
| 7 | ftipscontent | 帮助提示内容 | varchar | 200 |  | √ | ' ' | 帮助提示内容 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fconfigtype | 配置项类型 | varchar | 80 |  | √ | ' ' | 配置项类型,枚举: number :数值 text :文本 boolean :布尔 enum :枚举 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | osr_dispschbiztype_c_idx |  | fconfigname,fconfigkey |
| 2 | pk_t_osr_dispschbiztype_c |  | fentryid |
| 3 | osr_dispschbiztype_c_fid_idx |  | fid |

---

## 界面显示方案业务类型-多语言表 t_osr_dispschbiztype_l

- **表名称：** 界面显示方案业务类型-多语言表
- **表名：** t_osr_dispschbiztype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 240 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_osr_dispschbiztype_l |  | fpkid |
| 2 | idx_osr_dispschbiztype_l |  | fid,flocaleid |

---

## 依赖许可单据体-子表 t_osr_dispschbiztype_p

- **表名称：** 依赖许可单据体-子表
- **表名：** t_osr_dispschbiztype_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeplicensegroupid | 依赖许可分组id | int8 | 64 |  | √ | 0 | 依赖许可分组id |
| 3 | fcheckmethod | 校验方式 | varchar | 12 |  | √ | ' ' | 校验方式,枚举: and :唯一 or :任意 |
| 4 | fdeplicensemodule | 依赖许可所属模块 | varchar | 50 |  | √ | ' ' | 依赖许可所属模块 |
| 5 | fdeplicensemodulen | 依赖许可所属模块名称 | varchar | 80 |  | √ | ' ' | 依赖许可所属模块名称 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | flicensemodulename | 许可模块名称 | varchar | 80 |  | √ | ' ' | 许可模块名称 |
| 8 | flicensegroupname | 许可分组名称 | varchar | 80 |  | √ | ' ' | 许可分组名称 |
| 9 | flicensetype | 许可类型 | varchar | 12 |  | √ | ' ' | 许可类型,枚举: module :模块 kit :套件 |
| 10 | fdeplicensegroupn | 依赖许可分组名称 | varchar | 80 |  | √ | ' ' | 依赖许可分组名称 |
| 11 | flicensegroupid | 许可分组id | int8 | 64 |  | √ | 0 | 许可分组id |
| 12 | flicensemodule | 许可所属模块编码 | varchar | 50 |  | √ | ' ' | 许可所属模块编码 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_osr_dispschbiztype_p |  | fentryid |
| 2 | dispschbiztype_p_index |  | fid |

---

## 界面显示方案业务类型-主表 t_osr_dispschbiztype

- **表名称：** 界面显示方案业务类型-主表
- **表名：** t_osr_dispschbiztype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fshowlistconfig | 显示列表配置 | bpchar | 1 |  | √ | '1' | 显示列表配置 |
| 6 | flicensedpgroupid | 依赖许可分组id | int8 | 64 |  | √ | 0 | 依赖许可分组id |
| 7 | fshowopconfig | 显示功能配置 | bpchar | 1 |  | √ | '0' | 显示功能配置 |
| 8 | fshowareaconfig | 显示区域配置 | bpchar | 1 |  | √ | '0' | 显示区域配置 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fshowcommonconfig | 显示通用配置 | bpchar | 1 |  | √ | '0' | 显示通用配置 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | flicensedpmodule | 依赖许可所属模块 | varchar | 50 |  | √ | ' ' | 依赖许可所属模块 |
| 15 | flicensegroupid | 许可分组id | int8 | 64 |  | √ | 0 | 许可分组id |
| 16 | fshowdetaillistconfig | 显示明细列表配置 | bpchar | 1 |  | √ | '1' | 显示明细列表配置 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | flicensemodule | 许可所属模块 | varchar | 50 |  | √ | ' ' | 许可所属模块 |
| 20 | fshowinputconfig | 显示录入配置 | bpchar | 1 |  | √ | '1' | 显示录入配置 |
| 21 | fshowtype | 界面显示类型 | bpchar | 1 |  | √ | 'A' | 界面显示类型,枚举: A :移动端 B :平板端 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_osr_dispschbiztype |  | fnumber |
| 2 | pk_osr_dispschbiztype |  | fid |
