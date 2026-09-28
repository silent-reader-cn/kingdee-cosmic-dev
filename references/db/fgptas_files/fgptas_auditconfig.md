# 审核要素配置-fgptas_auditconfig

## 审核要素配置-主表 t_fgptas_auditconf

- **表名称：** 审核要素配置-主表
- **表名：** t_fgptas_auditconf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fattachkey | 附件标识 | varchar | 25 |  | √ | 'attachmentpanel' | 附件标识 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | findexmethod | 索引方式 | varchar | 50 |  | √ | ' ' | 索引方式,枚举: |
| 7 | fentityobject | 单据实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | fprocess | GPT任务 | int8 | 64 |  | √ | 0 | 任务流 gai_process |
| 9 | fbillnokey | 编码标识 | varchar | 25 |  | √ | 'billno' | 编码标识 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | ffgptasuser | GPT财务助手人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | fuserkey | 申请人标识 | varchar | 25 |  | √ | ' ' | 申请人标识 |
| 18 | fuserkeyfield | 申请人标识 | varchar | 25 |  | √ | ' ' | 申请人标识 |
| 19 | fprompt | GPT提示 | int8 | 64 |  | √ | 0 | GPT提示 gai_prompt |
| 20 | fembbedingtimeout | 同步等待向量化时间（毫秒） | int8 | 64 |  | √ | 20000 | 同步等待向量化时间（毫秒） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_auditconf_entity |  | fentityobject |
| 2 | pk_t_fgptas_auditconf |  | fid |

---

## 审核要素明细-子表 t_fgptas_element

- **表名称：** 审核要素明细-子表
- **表名：** t_fgptas_element

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frule | 规则 | varchar | 2000 |  | √ | ' ' | 规则 |
| 3 | frulebe | 规则（后台） | varchar | 2000 |  | √ | ' ' | 规则（后台） |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | felement | 审核要素 | varchar | 200 |  | √ | ' ' | 审核要素 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_element_0 |  | fid |
| 2 | pk_t_fgptas_element |  | fentryid |

---

## 审核要素配置-多语言表 t_fgptas_auditconf_l

- **表名称：** 审核要素配置-多语言表
- **表名：** t_fgptas_auditconf_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fgptas_auditconf_l |  | fpkid |
| 2 | idx_fgptas_auditconf_l_0 |  | fid,flocaleid |
