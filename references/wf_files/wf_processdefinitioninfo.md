# 流程定义操作信息-wf_processdefinitioninfo

## 流程定义操作信息-主表 t_wf_procdefinfo

- **表名称：** 流程定义操作信息-主表
- **表名：** t_wf_procdefinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentityname | 实体名称 | varchar | 255 |  | √ | ' ' | 实体名称 |
| 3 | factid | 节点 | varchar | 100 |  | √ | ' ' | 节点 |
| 4 | fentitynumber | 实体编码 | varchar | 100 |  | √ | ' ' | 实体编码 |
| 5 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 6 | finfojsonid | 流程定义资源ID | varchar | 255 |  | √ | ' ' | 流程定义资源ID |
| 7 | foperation | 操作 | varchar | 100 |  | √ | ' ' | 操作 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_procdefinfo_opr_entity |  | foperation,fentitynumber |
| 2 | t_wf_procdefinfo_pkey |  | fid |

---

## 流程定义操作信息-多语言表 t_wf_procdefinfo_l

- **表名称：** 流程定义操作信息-多语言表
- **表名：** t_wf_procdefinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentityname | 实体名称 | varchar | 255 |  | √ | ' ' | 实体名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_procdefinfo_l_pkey |  | fpkid |
| 2 | idx_wf_procdefinfo_l |  | fid,flocaleid |
