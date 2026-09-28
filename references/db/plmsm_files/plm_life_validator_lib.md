# 生命周期校验器-plm_life_validator_lib

## 生命周期校验器-多语言表 t_plmsm_lc_validator_lib_l

- **表名称：** 生命周期校验器-多语言表
- **表名：** t_plmsm_lc_validator_lib_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 校验器名称 | varchar | 50 |  | √ | ' ' | 校验器名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmsm_lc_validator_lib_l |  | fpkid |
| 2 | idx_plmsm_lc_validator_lib_l_0 |  | fid,flocaleid |

---

## 生命周期校验器-主表 t_plmsm_lc_validator_lib

- **表名称：** 生命周期校验器-主表
- **表名：** t_plmsm_lc_validator_lib

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 校验器名称 | varchar | 50 |  | √ | ' ' | 校验器名称 |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 校验器编码 | varchar | 30 |  | √ | ' ' | 校验器编码 |
| 10 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 11 | fclasspath | 校验器路径 | varchar | 255 |  | √ | ' ' | 校验器路径 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmsm_lc_validator_lib |  | fid |
| 2 | idx_plmsm_lc_val_lib_name |  | fname |
