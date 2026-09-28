# 余额表-bal_balanceinfo

## 余额表-主表 t_bal_balanceinfo

- **表名称：** 余额表-主表
- **表名：** t_bal_balanceinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 余额表元数据ID | varchar | 36 |  | √ | ' ' | 余额表元数据ID |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | fname | varchar | 200 |  | √ | ' ' |  |
| 4 | fsnapshottable | 快照表物理表 | varchar | 30 |  | √ | ' ' | 快照表物理表 |
| 5 | fpluginclass | 插件 | text | 0 |  |  | null | 插件 |
| 6 | fbalancetype | 余额类型 | varchar | 10 |  | √ | ' ' | 余额类型,枚举: realtime :即时余额 period :期间余额 |
| 7 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 8 | fsysstatus | 出厂状态 | bpchar | 1 |  | √ | '0' | 出厂状态,枚举: 0 :正常 1 :禁用 |
| 9 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fpkfieldname | 余额表主键字段 | varchar | 30 |  | √ | ' ' | 余额表主键字段 |
| 11 | fsnapshotpolicy | 快照方式 | bpchar | 1 |  | √ | 'A' | 快照方式,枚举: A :保留历史 B :只留最新 |
| 12 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
| 13 | ftablename | 余额表物理表 | varchar | 30 |  | √ | ' ' | 余额表物理表 |
| 14 | fistemplate | 模板 | bpchar | 1 |  | √ | '0' | 模板 |
| 15 | fupdatepolicy | 更新方式 | bpchar | 1 |  | √ | 'A' | 更新方式,枚举: A :同步 B :部分异步 C :完全异步 |
| 16 | ffields | 余额表字段 | text | 0 |  |  | null | 余额表字段 |
| 17 | fcuststatus | 用户状态 | bpchar | 1 |  | √ | '0' | 用户状态,枚举: 0 :启用 1 :禁用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bal_balanceinfo |  | fid |

---

## 余额表-多语言表 t_bal_balanceinfo_l

- **表名称：** 余额表-多语言表
- **表名：** t_bal_balanceinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | fnumber | fnumber | varchar | 36 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bal_balanceinfo_l |  | fpkid |
