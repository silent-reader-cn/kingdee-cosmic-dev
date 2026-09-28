# 技能运行数据-fatvs_skill_runtimedata

## 技能运行数据-多语言表 t_fatvs_skillruntimedata_l

- **表名称：** 技能运行数据-多语言表
- **表名：** t_fatvs_skillruntimedata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fatvs_skill_runtimedata_l |  | fid,flocaleid |
| 2 | pk_t_fatvs_skillruntimedata_l |  | fpkid |

---

## 运行数据-子表 t_fatvs_runtimedataentry

- **表名称：** 运行数据-子表
- **表名：** t_fatvs_runtimedataentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparamvalue | 参数值 | varchar | 50 |  | √ | ' ' | 参数值 |
| 3 | fparamname | 参数名 | varchar | 50 |  | √ | ' ' | 参数名 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fatvs_runtimedataentry |  | fentryid |
| 2 | idx_fatvs_skill_runtimeentry |  | fid |

---

## 技能运行数据-主表 t_fatvs_skillruntimedata

- **表名称：** 技能运行数据-主表
- **表名：** t_fatvs_skillruntimedata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fsavemoney | 节约资金 | numeric | 23 | 10 | √ | 0 | 节约资金 |
| 5 | flaborcost | 每月人工成本 | numeric | 23 | 10 | √ | 0 | 每月人工成本 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fruntimejson_tag | 运行数据json_详情 | text | 0 |  |  | null | 运行数据json_详情 |
| 8 | fpeoplework | 节约人效 | numeric | 23 | 10 | √ | 0 | 节约人效 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fbegintime | 查询时间段.开始 | timestamp | 0 |  |  | null | 查询时间段.开始 |
| 11 | foffice | 办公室 | int8 | 64 |  | √ | 0 | [办公室 fatvs_office](../fatvs_files/fatvs_office.md) |
| 12 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | ffailcount | 失败数据量 | int8 | 64 |  | √ | 0 | 失败数据量 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | femployee | 员工 | int8 | 64 |  | √ | 0 | [形象库 fatvs_employee](../fatvs_files/fatvs_employee.md) |
| 17 | fruntimejson | 运行数据json | varchar | 255 |  | √ | ' ' | 运行数据json |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | flaborefficiency | 每月人工处理任务数 | int8 | 64 |  | √ | 0 | 每月人工处理任务数 |
| 20 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 21 | ftotalcount | 总数量 | int8 | 64 |  | √ | 0 | 总数量 |
| 22 | fendtime | 查询时间段.结束 | timestamp | 0 |  |  | null | 查询时间段.结束 |
| 23 | fskill | 技能 | int8 | 64 |  | √ | 0 | [技能 fatvs_skill](../fatvs_files/fatvs_skill.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fatvs_skill_runtime_skill |  | fskill |
| 2 | idx_fatvs_skill_runtime_btime |  | fbegintime |
| 3 | idx_fatvs_skill_runtime_office |  | foffice |
| 4 | pk_t_fatvs_skillruntimedata |  | fid |
| 5 | idx_fatvs_skill_runtime_ee |  | femployee |
