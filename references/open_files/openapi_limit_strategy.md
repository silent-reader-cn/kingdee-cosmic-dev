# 限流策略-openapi_limit_strategy

## 限流策略-多语言表 t_open_rule_config_l

- **表名称：** 限流策略-多语言表
- **表名：** t_open_rule_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_rule_config_l |  | fpkid |
| 2 | idx_t_open_rule_config_l_fid |  | fid,flocaleid |

---

## 限流策略-主表 t_open_rule_config

- **表名称：** 限流策略-主表
- **表名：** t_open_rule_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fcontrolbehavior | 限流效果 | bpchar | 1 |  | √ | '0' | 限流效果,枚举: 0 :快速失败 1 :排队等候 TESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTE :TEST |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fstrategy | 规则策略 | bpchar | 1 |  | √ | '0' | 规则策略,枚举: 0 :流控 1 :熔断 |
| 7 | fdescription | 描述 | varchar | 200 |  |  | ' ' | 描述 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fresourcetype | 限流维度 | bpchar | 1 |  | √ | '0' | 限流维度,枚举: 0 :第三方应用 1 :API 2 :匿名访问 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 15 | fcount | 限流次数（次/秒） | int4 | 32 |  | √ | 0 | 限流次数（次/秒） |
| 16 | fgrade | 流控类型 | bpchar | 1 |  | √ | '1' | 流控类型,枚举: 0 :线程 1 :QPS |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_rule_config_fnumber |  | fnumber |
| 2 | pk_t_open_rule_config |  | fid |

---

## 限流清单-子表 t_open_rule_config_detail

- **表名称：** 限流清单-子表
- **表名：** t_open_rule_config_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flimitapp | 限制应用 | varchar | 100 |  | √ | ' ' | 限制应用 |
| 3 | fthirdid | 第三方应用编码 | int8 | 64 |  | √ | 0 | 第三方应用 third_app |
| 4 | fappname | 服务应用 | varchar | 100 |  | √ | ' ' | 服务应用 |
| 5 | fapiid | API编码 | int8 | 64 |  | √ | 0 | API服务 openapi_apilist |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fresource | 资源 | varchar | 200 |  | √ | ' ' | 资源 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rule_config_detail_resouce |  | fresource |
| 2 | pk_t_open_rule_config_detail |  | fentryid |
| 3 | idx_rule_config_id |  | fid |
