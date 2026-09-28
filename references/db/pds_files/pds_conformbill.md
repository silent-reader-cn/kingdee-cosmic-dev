# 合规检查结果-pds_conformbill

## 合规检查结果-多语言表 t_pds_conformbill_l

- **表名称：** 合规检查结果-多语言表
- **表名：** t_pds_conformbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnodename | 当前节点名称 | varchar | 100 |  | √ | ' ' | 当前节点名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fbillname | 项目名称 | varchar | 300 |  | √ | ' ' | 项目名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_conformbill_l_fid_lid |  | fid,flocaleid |
| 2 | pk_pds_conformbill_l |  | fpkid |

---

## 检查项分录-子表 t_pds_conformresult

- **表名称：** 检查项分录-子表
- **表名：** t_pds_conformresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontroltype | fcontroltype | bpchar | 1 |  | √ | ' ' |  |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fnote | 确认说明 | varchar | 255 |  | √ | ' ' | 确认说明 |
| 5 | fdescription | 检查详情 | varchar | 1024 |  | √ | ' ' | 检查详情 |
| 6 | fsysresultid | 系统检查结果 | int8 | 64 |  | √ | 0 | [评估等级 bd_evagrade](../basedata_files/bd_evagrade.md) |
| 7 | fcheckitemid | 检查项 | int8 | 64 |  | √ | 0 | [合规方案检查项F7 pds_conformitemf7](../pds_files/pds_conformitemf7.md) |
| 8 | flogtype | flogtype | bpchar | 1 |  | √ | ' ' |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fpluginname | fpluginname | varchar | 100 |  | √ | ' ' |  |
| 11 | fresultid | 确认检查结果 | int8 | 64 |  | √ | 0 | [评估等级 bd_evagrade](../basedata_files/bd_evagrade.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_conformresult |  | fentryid |
| 2 | idx_pds_conformresult_fid |  | fid |

---

## 模板分录-子表 t_src_projecttpl

- **表名称：** 模板分录-子表
- **表名：** t_src_projecttpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomponentid | 业务组件 | int8 | 64 |  | √ | 0 | [组件注册 pds_compreg](../pds_files/pds_compreg.md) |
| 3 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | [组件模板配置 pds_tplconfig](../pds_files/pds_tplconfig.md) |
| 4 | fbizobject | 业务对象 | varchar | 50 |  | √ | ' ' | 业务对象 |
| 5 | fsrctplid | 来源模板ID | varchar | 50 |  | √ | ' ' | 来源模板ID |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_projecttpl_fscp |  | fsrctplid |
| 2 | idx_src_projecttpl_fobj |  | fbizobject |
| 3 | idx_src_projecttpl_fcom |  | fcomponentid |
| 4 | pk_src_projecttpl |  | fentryid |
| 5 | idx_src_projecttpl_fid |  | fid |
| 6 | idx_src_projecttpl_ftem |  | ftemplateid |

---

## 合规检查结果-主表 t_pds_conformbill

- **表名称：** 合规检查结果-主表
- **表名：** t_pds_conformbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcbillno | 项目编号 | varchar | 80 |  | √ | ' ' | 项目编号 |
| 3 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fschemeid | 合规管控方案 | int8 | 64 |  | √ | 0 | [合规管控方案 src_conformscheme](../pds_files/src_conformscheme.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fcreatorid | 检查人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | foperation | 业务操作 | varchar | 30 |  | √ | ' ' | 业务操作,枚举: submit :提交 audit :审核 allopen :开标 tecopen :开技术标 bizopen :开商务标 aptopen :开资审标 |
| 8 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 9 | fresultid | 确认检查结果 | int8 | 64 |  | √ | 0 | [评估等级 bd_evagrade](../basedata_files/bd_evagrade.md) |
| 10 | ftemplate | 组件模板 | int8 | 64 |  | √ | 0 | [组件模板配置 pds_tplconfig](../pds_files/pds_tplconfig.md) |
| 11 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbillstatus | 确认状态 | bpchar | 1 |  | √ | 'A' | 确认状态,枚举: A :待确认 B :已提交 C :已确认 |
| 14 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 15 | fcreatetime | 检查时间 | timestamp | 0 |  |  | null | 检查时间 |
| 16 | fbizobject | 业务对象 | varchar | 30 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 17 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 18 | fcontroltype | 控制强度 | bpchar | 1 |  | √ | ' ' | 控制强度,枚举: 0 :不控制 1 :提醒 2 :禁止 |
| 19 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fauditdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 21 | fsysresultid | 系统检查结果 | int8 | 64 |  | √ | 0 | [评估等级 bd_evagrade](../basedata_files/bd_evagrade.md) |
| 22 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 23 | fbillname | 项目名称 | varchar | 300 |  | √ | ' ' | 项目名称 |
| 24 | fnodename | 当前节点名称 | varchar | 100 |  | √ | ' ' | 当前节点名称 |
| 25 | fauditorid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_conformbill |  | fid |
| 2 | idx_pds_conformbill_sid |  | fsrcbillid |
| 3 | idx_pds_conformbill_id_obj_op |  | fsrcbillid,fbizobject,foperation |
| 4 | idx_pds_conformbill_id_obj |  | fsrcbillid,fbizobject |

---

## 消息接收人-多选基础资料表 t_pds_conformuser

- **表名称：** 消息接收人-多选基础资料表
- **表名：** t_pds_conformuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_conformuser_fid |  | fid |
| 2 | pk_pds_conformuser |  | fpkid |
| 3 | idx_pds_conformuser_bid |  | fbasedataid |
