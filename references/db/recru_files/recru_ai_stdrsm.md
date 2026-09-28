# ai标准简历知识库-recru_ai_stdrsm

## ai标准简历知识库-主表 t_recru_ai_stdrsm

- **表名称：** ai标准简历知识库-主表
- **表名：** t_recru_ai_stdrsm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | flabel | 标签 | varchar | 100 |  | √ | ' ' | 标签 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fknowledgeconfigid | 知识库配置 | int8 | 64 |  | √ | 0 | [ai招聘结构化知识库 recru_ai_knowledge](../recru_files/recru_ai_knowledge.md) |
| 6 | finitstatus | 初始化状态 | varchar | 2 |  | √ | ' ' | 初始化状态,枚举: 0 :进行中 1 :已验证 2 :已完成 |
| 7 | finitbatch | 初始化批次 | int8 | 64 |  | √ | 0 | 初始化批次 |
| 8 | ftpsys | 第三方系统 | varchar | 50 |  | √ | ' ' | 第三方系统,枚举: KD :金蝶 MK :摩卡 BS :北森 DY :大易 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: success :成功 failed :失败 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | ftptenantid | 第三方租户ID | varchar | 50 |  | √ | ' ' | 第三方租户ID |
| 13 | ftpdatanum | 第三方数据编码 | varchar | 50 |  | √ | ' ' | 第三方数据编码 |
| 14 | fstdrsmid | ai标准简历 | int8 | 64 |  | √ | 0 | [标准简历 recru_standardresume](../recru_files/recru_standardresume.md) |
| 15 | finitdatasource | 数据来源 | varchar | 2 |  | √ | ' ' | 数据来源,枚举: 0 :手工录入 1 :初始化 2 :外部集成 |
| 16 | ftpdataid | 第三方数据ID | varchar | 50 |  | √ | ' ' | 第三方数据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_ai_stdrsm |  | fid |
| 2 | idx_recru_ai_stdrsm_std |  | fstdrsmid |
