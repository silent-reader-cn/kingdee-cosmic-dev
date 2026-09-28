# 生成QA对方案-aikm_genqa_scheme

## 生成QA对方案-主表 t_aikm_genqa_scheme

- **表名称：** 生成QA对方案-主表
- **表名：** t_aikm_genqa_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | fscenetype | 场景类型 | varchar | 50 |  | √ | ' ' | 场景类型 |
| 6 | fcontextual | 场景化问题 | bpchar | 1 |  | √ | '0' | 场景化问题 |
| 7 | fconceptual | 概念性问题 | bpchar | 1 |  | √ | '0' | 概念性问题 |
| 8 | fgencount | 生成数量 | int4 | 32 |  | √ | 0 | 生成数量 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fprocedural | 操作性问题 | bpchar | 1 |  | √ | '0' | 操作性问题 |
| 14 | fcoverarea | 覆盖领域 | varchar | 1500 |  | √ | ' ' | 覆盖领域 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fcontentmodel | 内容模式 | int4 | 32 |  | √ | 0 | 内容模式 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | fprompt | 提示词 | varchar | 2000 |  | √ | ' ' | 提示词 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_aikm_genqa_scheme |  | fname |
| 2 | pk_t_aikm_genqa_scheme |  | fid |

---

## 生成QA对方案-多语言表 t_aikm_genqa_scheme_l

- **表名称：** 生成QA对方案-多语言表
- **表名：** t_aikm_genqa_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aikm_genqa_scheme_l |  | fpkid |
| 2 | idx_t_aikm_genqa_scheme_l |  | fid,flocaleid |
