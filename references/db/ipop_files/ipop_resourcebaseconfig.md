# 资源基础资料配置-ipop_resourcebaseconfig

## 资源清单单据体-子表 t_ipop_resourcelistentity

- **表名称：** 资源清单单据体-子表
- **表名：** t_ipop_resourcelistentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbuymoresys | 增购对接系统 | varchar | 50 |  | √ | ' ' | 增购对接系统,枚举: otp :OTP yzj :云之家 wechat :企业微信 |
| 3 | fcrosssystem | 跨系统资源 | varchar | 50 |  | √ | '0' | 跨系统资源 |
| 4 | ftag | 标签 | varchar | 255 |  | √ | ' ' | 标签 |
| 5 | fnolimit | 不限量 | varchar | 1 |  | √ | '0' | 不限量 |
| 6 | ftag_tag | 标签_详情 | text | 0 |  |  | null | 标签_详情 |
| 7 | funitid | 显示单位 | int8 | 64 |  | √ | 0 | [资源辅助资料 ipop_resauxiliarydata](../ipop_files/ipop_resauxiliarydata.md) |
| 8 | fshowinresource | 资源用量中显示 | varchar | 1 |  | √ | '0' | 资源用量中显示 |
| 9 | fbuymore | 显示增购 | varchar | 1 |  | √ | '0' | 显示增购 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fshowusedetail | 显示使用明细 | varchar | 1 |  | √ | '0' | 显示使用明细 |
| 12 | fwarning | 预警提醒 | varchar | 1 |  | √ | '0' | 预警提醒 |
| 13 | fdseq | 显示次序 | int4 | 32 |  | √ | 1 | 显示次序 |
| 14 | fimplclass | 取值逻辑类 | varchar | 255 |  | √ | ' ' | 取值逻辑类 |
| 15 | fmodulename | 模块名称 | varchar | 50 |  | √ | ' ' | 模块名称 |
| 16 | fsimplecode | 模块简码 | varchar | 50 |  | √ | ' ' | 模块简码 |
| 17 | fthresholdtype | 阈值类型 | varchar | 50 |  | √ | ' ' | 阈值类型,枚举: |
| 18 | fclassificationid | 展示栏位 | int8 | 64 |  | √ | 0 | [资源辅助资料 ipop_resauxiliarydata](../ipop_files/ipop_resauxiliarydata.md) |
| 19 | fspecifications | 默认规格 | numeric | 23 | 10 | √ | 0 | 默认规格 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fmodulenumber | 模块编码 | varchar | 50 |  | √ | ' ' | 模块编码 |
| 22 | fwarningvalue | 余量预警值 | int8 | 64 |  | √ | 0 | 余量预警值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipop_resourcelistentity |  | fentryid |
| 2 | idx_ipop_resourcelistentity_id |  | fid |

---

## 资源基础资料配置-主表 t_ipop_resourcebaseconfig

- **表名称：** 资源基础资料配置-主表
- **表名：** t_ipop_resourcebaseconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fprodname | 产品名称 | varchar | 50 |  | √ | ' ' | 产品名称 |
| 6 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fproductid | 产品系列 | int8 | 64 |  | √ | 0 | [资源辅助资料 ipop_resauxiliarydata](../ipop_files/ipop_resauxiliarydata.md) |
| 8 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fdeploymode | 部署方式 | varchar | 50 |  | √ | ' ' | 部署方式,枚举: public :公有云 private :私有云 |
| 10 | flicenseclass | 资源许可实现类 | varchar | 2000 |  | √ | ' ' | 资源许可实现类 |
| 11 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipop_resourcebaseconfig |  | fid |
| 2 | idx_ipop_resourcebaseconfig_version |  | fversion |
