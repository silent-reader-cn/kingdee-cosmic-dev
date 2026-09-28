# 场景输出参数操作记录-plm_rengine_sceneoutput_h

## 场景输出参数操作记录-多语言表 t_plm_egn_sceneoutput_his_l

- **表名称：** 场景输出参数操作记录-多语言表
- **表名：** t_plm_egn_sceneoutput_his_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 场景输出参数名称 | varchar | 100 |  | √ | ' ' | 场景输出参数名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_egn_sceneoutput_his_l |  | fpkid |
| 2 | idx_plm_sceneoutput_his_l |  | fid,flocaleid |

---

## 场景输出参数操作记录-主表 t_plm_egn_sceneoutput_his

- **表名称：** 场景输出参数操作记录-主表
- **表名：** t_plm_egn_sceneoutput_his

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperate | 操作 | varchar | 20 |  | √ | ' ' | 操作,枚举: new :新增 modify :修改 delete :删除 |
| 3 | fname | 场景输出参数名称 | varchar | 50 |  | √ | ' ' | 场景输出参数名称 |
| 4 | foperatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fscenenumber | 所属场景编码 | varchar | 50 |  | √ | ' ' | 所属场景编码 |
| 6 | fsceneid | 所属场景id | int8 | 64 |  | √ | 0 | 所属场景id |
| 7 | fsceneoutputid | 场景输出参数id | int8 | 64 |  | √ | 0 | 场景输出参数id |
| 8 | foperatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 9 | fnumber | 场景输出参数编码 | varchar | 50 |  | √ | ' ' | 场景输出参数编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_egn_sceneoutput_his |  | fid |
| 2 | idx_plm_sceneoutput_his |  | fnumber |
