# 余额更新规则列表-bal_balanceupdaterule

## 余额更新规则列表-多语言表 t_bal_updateruledesign_l

- **表名称：** 余额更新规则列表-多语言表
- **表名：** t_bal_updateruledesign_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | fnumber | fnumber | varchar | 36 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdata | fdata | text | 0 |  |  | null |  |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bal_updateruledesign_l |  | fpkid |

---

## 余额更新规则列表-主表 t_bal_updateruledesign

- **表名称：** 余额更新规则列表-主表
- **表名：** t_bal_updateruledesign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 4 | fmodeltype | fmodeltype | varchar | 50 |  | √ | ' ' |  |
| 5 | fparentid | 父规则 | varchar | 36 |  | √ | ' ' | 余额更新规则列表 bal_balanceupdaterule |
| 6 | fisv | 开发商 | varchar | 50 |  | √ | ' ' | 开发商 |
| 7 | fbalancetablenumber | 余额表 | varchar | 36 |  | √ | ' ' | 余额表 bal_balanceinfo |
| 8 | finheritpath | finheritpath | varchar | 300 |  | √ | ' ' |  |
| 9 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 10 | fsysstatus | 出厂状态 | bpchar | 1 |  | √ | '0' | 出厂状态,枚举: 0 :正常 1 :禁用 |
| 11 | fcreatedate | fcreatedate | timestamp | 0 |  |  | LOCALTIMESTAMP |  |
| 12 | fmasterid | 原始规则 | varchar | 36 |  | √ | ' ' | 余额更新规则列表 bal_balanceupdaterule |
| 13 | ftype | 扩展状态 | bpchar | 1 |  | √ | '0' | 扩展状态,枚举: 0 :原始规则 1 :派生规则 2 :扩展规则 |
| 14 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fnumber | 编码 | varchar | 36 |  |  | null | 编码 |
| 16 | fdata | fdata | text | 0 |  |  | null |  |
| 17 | ftimestamp | ftimestamp | int8 | 64 |  | √ | 0 |  |
| 18 | fistemplate | fistemplate | bpchar | 1 |  | √ | '0' |  |
| 19 | fsourceentitynumber | 源单 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 20 | fversion | fversion | int8 | 64 |  | √ | 0 |  |
| 21 | fcuststatus | fcuststatus | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bal_updateruledesign |  | fid |

---

## 余额更新规则列表-分表 t_bal_updateruledesign_s

- **表名称：** 余额更新规则列表-分表
- **表名：** t_bal_updateruledesign_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fcuststatus | 启用状态 | bpchar | 1 |  | √ | '0' | 启用状态,枚举: 1 :启用 2 :禁用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bal_updateruledesign_s |  | fid |
| 2 | idx_bal_updateruledesign_s |  | fcuststatus |
