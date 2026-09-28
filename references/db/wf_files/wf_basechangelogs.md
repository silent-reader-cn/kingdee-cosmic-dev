# 日志变更记录-wf_basechangelogs

## 日志变更记录-主表 t_wf_basechangelogs

- **表名称：** 日志变更记录-主表
- **表名：** t_wf_basechangelogs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftitle | 标题 | varchar | 230 |  | √ | ' ' | 标题 |
| 3 | fbaseformid | 基础资料id | int8 | 64 |  | √ | 0 | 基础资料id |
| 4 | fdetail | 内容 | text | 0 |  |  | null | 内容 |
| 5 | ftype | 基础资料类型 | varchar | 30 |  | √ | ' ' | 基础资料类型,枚举: admin :流程管理员 role :工作流角色 orgtype :组织类型 comment :常用审批意见 attribute :单据流程属性 summary :移动单据摘要 |
| 6 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fop | 操作 | varchar | 30 |  | √ | ' ' | 操作,枚举: insert :新增 modify :修改 delete :删除 enable :启用 disable :禁用 importdata :导入 exportlist :导出 |
| 8 | fshowdetail | fshowdetail | varchar | 1000 |  | √ | ' ' |  |
| 9 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_basechangelogs_pkey |  | fid |
| 2 | idx_wf_basechangelogs |  | fbaseformid |

---

## 日志变更记录-多语言表 t_wf_basechangelogs_l

- **表名称：** 日志变更记录-多语言表
- **表名：** t_wf_basechangelogs_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 标题 | varchar | 230 |  | √ | ' ' | 标题 |
| 3 | fdetail | 内容 | text | 0 |  |  | null | 内容 |
| 4 | fshowdetail | 内容 | varchar | 1000 |  | √ | ' ' | 内容 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_basechangelogs_l |  | fid,flocaleid |
| 2 | t_wf_basechangelogs_l_pkey |  | fpkid |
