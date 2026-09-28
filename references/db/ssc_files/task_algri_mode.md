# AI算法管理-task_algri_mode

## AI算法管理-主表 t_tk_approve_algorithm

- **表名称：** AI算法管理-主表
- **表名：** t_tk_approve_algorithm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fthreshold | 阈值 | numeric | 23 | 10 | √ | 0 | 阈值 |
| 4 | frecallrate | 召回率 | numeric | 23 | 10 | √ | 0 | 召回率 |
| 5 | fnewrecommend_tag | 推荐值_详情 | text | 0 |  |  | null | 推荐值_详情 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauc | auc值 | numeric | 23 | 10 | √ | 0 | auc值 |
| 8 | faccuracy | 准确率 | numeric | 23 | 10 | √ | 0 | 准确率 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | frecommend | 推荐值(旧) | varchar | 1000 |  | √ | ' ' | 推荐值(旧) |
| 11 | fstatus | 数据状态 | varchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | flasttraintime | 最近一次训练时间 | timestamp | 0 |  |  | null | 最近一次训练时间 |
| 15 | fservicename | 服务名称 | varchar | 50 |  | √ | ' ' | 服务名称 |
| 16 | fmodelname | 模型名称 | varchar | 50 |  | √ | ' ' | 模型名称 |
| 17 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 19 | ftrainsize | 训练数据量 | int4 | 32 |  | √ | 0 | 训练数据量 |
| 20 | fusedtimes | 服务调用次数 | int4 | 32 |  | √ | 0 | 服务调用次数 |
| 21 | fnewrecommend | 推荐值 | varchar | 255 |  | √ | ' ' | 推荐值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_appralgo_number |  | fnumber |
| 2 | pk_t_tk_approve_algorithm |  | fid |

---

## AI算法管理-多语言表 t_tk_approve_algorithm_l

- **表名称：** AI算法管理-多语言表
- **表名：** t_tk_approve_algorithm_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 300 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_approve_algorithm_l |  | fpkid |
| 2 | idx_ssc_smart_appralgo_l |  | fid,flocaleid |

---

## 影响因素分录-子表 t_tk_algri_influentry

- **表名称：** 影响因素分录-子表
- **表名：** t_tk_algri_influentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | ffactorinflurate | 因素影响占比 | numeric | 23 | 10 | √ | 0 | 因素影响占比 |
| 4 | finfluencefactor | 影响因素 | varchar | 50 |  | √ | ' ' | 影响因素 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | frecommend | frecommend | varchar | 300 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_algri_influentry |  | fentryid |
| 2 | idx_ssc_appralgo_factor |  | finfluencefactor |
