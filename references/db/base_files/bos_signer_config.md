# ID生成-配置中心-bos_signer_config

## ID生成-配置中心-多语言表 t_signer_config_l

- **表名称：** ID生成-配置中心-多语言表
- **表名：** t_signer_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
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
| 1 | idx_t_signer_config_l_fid |  | fid,flocaleid |
| 2 | pk_t_signer_config_l |  | fpkid |
| 3 | idx_t_signer_config_l_fname |  | fname |

---

## ID生成-配置中心-主表 t_signer_config

- **表名称：** ID生成-配置中心-主表
- **表名：** t_signer_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fstep | 步长 | int4 | 32 |  | √ | 0 | 步长 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fsegmentlength | 号段长度 | int8 | 64 |  | √ | 0 | 号段长度 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fiscompensate | 断号补偿 | bpchar | 1 |  | √ | '0' | 断号补偿 |
| 8 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | finitnumber | 初始ID | int8 | 64 |  | √ | 0 | 初始ID |
| 10 | fmasterid | 主数据内码 | varchar | 36 |  | √ | ' ' | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fkey | 关键字 | varchar | 512 |  | √ | ' ' | 关键字 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_signer_config_key |  | fkey |
| 2 | pk_t_signer_config |  | fid |
