# 节点模板变更日志-wf_nodetemplatelog

## 节点模板变更日志-主表 t_wf_nodetemplatelog

- **表名称：** 节点模板变更日志-主表
- **表名：** t_wf_nodetemplatelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 模板名称 | varchar | 500 |  | √ | ' ' | 模板名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | foldvalue_tag | 修改前_详情 | text | 0 |  |  | null | 修改前_详情 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | foldvalue | 修改前 | varchar | 255 |  | √ | ' ' | 修改前 |
| 7 | fnewvalue | 修改后 | varchar | 255 |  | √ | ' ' | 修改后 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fgroup | 模板分组 | int8 | 64 |  | √ | 0 | [节点模板分组 wf_nodetemplategroup](../wf_files/wf_nodetemplategroup.md) |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 模板编码 | varchar | 30 |  | √ | ' ' | 模板编码 |
| 15 | fnewvalue_tag | 修改后_详情 | text | 0 |  |  | null | 修改后_详情 |
| 16 | foperation | 操作 | varchar | 50 |  | √ | ' ' | 操作,枚举: add :新增 changebaseinfo :修改基本信息 delete :删除 import :导入 abled :启用 disabled :禁用 changeproperty :修改节点属性 |
| 17 | fnodetemplateid | 节点模板id | int8 | 64 |  | √ | 0 | 节点模板id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_nodetpllog_number |  | fnumber |
| 2 | pk_wf_nodetemplatelog |  | fid |

---

## 节点模板变更日志-多语言表 t_wf_nodetemplatelog_l

- **表名称：** 节点模板变更日志-多语言表
- **表名：** t_wf_nodetemplatelog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模板名称 | varchar | 500 |  | √ | ' ' | 模板名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_nodetemplatelog_l |  | fpkid |
| 2 | idx_wf_nodetemplatelog_l |  | fid,flocaleid |
