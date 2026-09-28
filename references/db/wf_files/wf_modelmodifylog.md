# 历史修改记录-wf_modelmodifylog

## 历史修改记录-主表 t_wf_modelmodifylog

- **表名称：** 历史修改记录-主表
- **表名：** t_wf_modelmodifylog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | foldval | 修改前 | varchar | 2000 |  | √ | ' ' | 修改前 |
| 5 | felementtypename | 节点类型名称 | varchar | 50 |  | √ | ' ' | 节点类型名称 |
| 6 | fschemeid | 方案ID | int8 | 64 |  | √ | 0 | 流程动态方案配置 wf_processdynamicconfig |
| 7 | fprocdefid | 流程定义 | int8 | 64 |  | √ | 0 | 流程管理 wf_processdefinition |
| 8 | fproperty | 属性编码 | varchar | 50 |  | √ | ' ' | 属性编码 |
| 9 | felementid | 节点ID | varchar | 255 |  | √ | ' ' | 节点ID |
| 10 | felement | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 11 | fgroupname | 属性分组名称 | varchar | 150 |  | √ | ' ' | 属性分组名称 |
| 12 | fprocnum | 流程编码 | varchar | 255 |  | √ | ' ' | 流程编码 |
| 13 | felementtype | 节点类型 | varchar | 50 |  | √ | ' ' | 节点类型 |
| 14 | ftype | 类型 | varchar | 15 |  | √ | ' ' | 类型 |
| 15 | foldval_tag | 修改前_详情 | text | 0 |  |  | null | 修改前_详情 |
| 16 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fcontent_tag | 修改后_详情 | text | 0 |  |  | null | 修改后_详情 |
| 18 | fgroup | 属性分组 | varchar | 50 |  | √ | ' ' | 属性分组 |
| 19 | frevision | 第几次修改 | int8 | 64 |  | √ | 0 | 第几次修改 |
| 20 | foperation | 操作类型 | varchar | 10 |  | √ | ' ' | 操作类型,枚举: add :新增 replace :修改 delete :删除 |
| 21 | fcontent | 修改后 | varchar | 2000 |  | √ | ' ' | 修改后 |
| 22 | fpropertyname | 属性名称 | varchar | 150 |  | √ | ' ' | 属性名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_modelmodifylog |  | fprocdefid |
| 2 | pk_wf_modelmodifylog |  | fid |
| 3 | idx_wf_modelmlog_schemetype |  | fschemeid,ftype |

---

## 历史修改记录-多语言表 t_wf_modelmodifylog_l

- **表名称：** 历史修改记录-多语言表
- **表名：** t_wf_modelmodifylog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | felementtypename | 节点类型名称 | varchar | 50 |  | √ | ' ' | 节点类型名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | felement | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 7 | fpropertyname | 属性名称 | varchar | 150 |  | √ | ' ' | 属性名称 |
| 8 | fgroupname | 属性分组名称 | varchar | 150 |  | √ | ' ' | 属性分组名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_modelmodifylog_l |  | fpkid |
| 2 | idx_wf_modelmodifylog_l |  | fid,flocaleid |
