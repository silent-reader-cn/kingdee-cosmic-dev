# 引入任务-iptm_imptask

## 目标业务对象-多选基础资料表 t_iptm_mitask_targetmeta

- **表名称：** 目标业务对象-多选基础资料表
- **表名：** t_iptm_mitask_targetmeta

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 目标业务对象列表 iptm_importtarget |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iptm_tk_fidbdid |  | fid,fbasedataid |
| 2 | pk_iptm_mitask_targetmeta |  | fpkid |

---

## 引入任务-多语言表 t_iptm_mitask_l

- **表名称：** 引入任务-多语言表
- **表名：** t_iptm_mitask_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iptm_mitask_l |  | fpkid |
| 2 | idx_iptm_tkl_fidflid |  | fid,flocaleid |

---

## 引入任务-主表 t_iptm_mitask

- **表名称：** 引入任务-主表
- **表名：** t_iptm_mitask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fimpstatus | 任务状态 | bpchar | 1 |  | √ | ' ' | 任务状态,枚举: A :暂存 B :执行中 C :引入成功 D :引入失败 E :已关闭 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodelinfo | 模板信息 | varchar | 255 |  | √ | ' ' | 模板信息 |
| 7 | fschemeid | 引入方案 | int8 | 64 |  | √ | 0 | 引入方案详情 iptm_scheme |
| 8 | fmodifytime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 9 | fmodelinfo_tag | 模板信息_详情 | text | 0 |  |  | null | 模板信息_详情 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  |  | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fschememodtime | 方案修改时间 | timestamp | 0 |  |  | null | 方案修改时间 |
| 14 | fserviceid | 后台引入服务id | varchar | 255 |  | √ | ' ' | 后台引入服务id |
| 15 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipmt_tk_num |  | fnumber |
| 2 | idx_ipmt_tk_scheme |  | fschemeid |
| 3 | idx_ipmt_tk_modtime |  | fmodifytime |
| 4 | pk_iptm_mitask |  | fid |
| 5 | idx_ipmt_tk_createtime |  | fcreatetime |

---

## 重传附件-附件表 t_iptm_mitaskentry_oatt

- **表名称：** 重传附件-附件表
- **表名：** t_iptm_mitaskentry_oatt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iptm_mitaskentry_oatt |  | fpkid |
| 2 | idx_iptm_tkeatt_bdid |  | fentryid,fbasedataid |

---

## 引入任务分录-子表 t_iptm_mitaskentry

- **表名称：** 引入任务分录-子表
- **表名：** t_iptm_mitaskentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frelpropname | 多Sheet页关联识别的唯一值 | varchar | 255 |  | √ | ' ' | 多Sheet页关联识别的唯一值 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | freplacekeyfield | 数据替换规则的唯一值 | varchar | 500 |  | √ | ' ' | 数据替换规则的唯一值 |
| 5 | freason | 失败原因 | varchar | 1000 |  | √ | ' ' | 失败原因 |
| 6 | flogid | 失败日志id | int8 | 64 |  | √ | 0 | 失败日志id |
| 7 | ftempurl | 预引入数据缓存地址 | varchar | 512 |  | √ | ' ' | 预引入数据缓存地址 |
| 8 | fsourcesheet | 指定 Sheet 页签 | varchar | 255 |  | √ | ' ' | 指定 Sheet 页签 |
| 9 | ffailcount | 失败数量 | numeric | 23 | 10 | √ | 0 | 失败数量 |
| 10 | fexecstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :暂存 B :执行中 C :引入成功 D :引入失败 E :已关闭 |
| 11 | fbillentityid | 目标业务对象 | int8 | 64 |  | √ | 0 | 目标业务对象列表 iptm_importtarget |
| 12 | fcount | 引入数据数量 | numeric | 23 | 10 | √ | 0 | 引入数据数量 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fimporttype | 引入方式 | varchar | 50 |  | √ | ' ' | 引入方式,枚举: new :添加新数据 override :更新已有数据 overridenew :更新已有数据并添加新数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iptm_mitaskentry |  | fentryid |
| 2 | idx_iptm_tkentry_entity |  | fbillentityid |
| 3 | idx_iptm_tkentry_id |  | fid |

---

## 字段映射-子表 t_iptm_mitaskdetail

- **表名称：** 字段映射-子表
- **表名：** t_iptm_mitaskdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffieldnumber | 字段编码 | varchar | 255 |  | √ | ' ' | 字段编码 |
| 2 | fmustinput | 必录 | bpchar | 1 |  | √ | '0' | 必录,枚举: 1 :必录 |
| 3 | ffieldname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fstdpartname | 实体字段分组 | varchar | 50 |  | √ | ' ' | 实体字段分组 |
| 8 | ftextfield | 文档内字段 | varchar | 255 |  | √ | ' ' | 文档内字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iptm_mitaskdetail |  | fdetailid |
| 2 | idx_iptm_tkdetail_enid |  | fentryid |
| 3 | idx_iptm_tkdetail_fdnum |  | ffieldnumber |
